import asyncio
import shutil
import tempfile
from pathlib import Path
from resemble.aio.servicers import Routable
from resemble.consensus.local_envoy import (
    ENVOY_CONFIG_TEMPLATE_NAME,
    LOCALHOST_DIRECT_CRT,
    LOCALHOST_DIRECT_KEY,
    LocalEnvoy,
)
from typing import Optional


class ExecutableLocalEnvoy(LocalEnvoy):

    def __init__(
        self,
        *,
        published_port: int,
        consensus_ports: list[int],
        websocket_ports: list[int],
        application_id: str,
        routables: list[Routable],
        base64_encoded_proto_desc_set: bytes,
        use_tls: bool,
        certificate: Optional[str],
        key: Optional[str],
        debug_mode: bool,
    ):
        self._published_port = published_port
        self._container_id: Optional[str] = None
        self._debug_mode = debug_mode

        service_names = [r.service_name() for r in routables]

        # Generate envoy config and write it to temporary files that get
        # cleaned up on .stop(). We copy all files without their metadata
        # to ensure that they are readable by the envoy user.
        self._tmp_envoy_dir = tempfile.TemporaryDirectory()
        self._tmp_envoy_config = f'{self._tmp_envoy_dir.name}/envoy.yaml'
        self._tmp_envoy_crt = f'{self._tmp_envoy_dir.name}/tls.crt'
        self._tmp_envoy_key = f'{self._tmp_envoy_dir.name}/tls.key'

        # These are the directories that Envoy will observe these files in.
        self._envoy_dir_name = self._tmp_envoy_dir.name
        self._envoy_config = f'{self._envoy_dir_name}/envoy.yaml'
        self._envoy_crt = f'{self._envoy_dir_name}/tls.crt'
        self._envoy_key = f'{self._envoy_dir_name}/tls.key'

        self._use_tls = use_tls

        # The port we run Envoy on is the port the user has requested to
        # send traffic to!
        self._port = self._published_port
        self._proxied_server_host = 'localhost'

        Path(self._tmp_envoy_config).write_text(
            self._generate_envoy_yaml(
                proxied_server_host=self._proxied_server_host,
                envoy_port=self._port,
                consensus_ports=consensus_ports,
                websocket_ports=websocket_ports,
                application_id=application_id,
                service_names=service_names,
                proto_descriptor_bin=base64_encoded_proto_desc_set,
                template_path=ENVOY_CONFIG_TEMPLATE_NAME,
                use_tls=self._use_tls,
                tls_certificate_path=self._envoy_crt,
                tls_key_path=self._envoy_key,
            )
        )

        if self._use_tls:
            shutil.copyfile(
                certificate or LOCALHOST_DIRECT_CRT,
                self._tmp_envoy_crt,
            )

            shutil.copyfile(
                key or LOCALHOST_DIRECT_KEY,
                self._tmp_envoy_key,
            )

        self._process: Optional[asyncio.subprocess.Process] = None

    @property
    def port(self) -> int:
        """Returns the port of the Envoy proxy.
        """
        if self._published_port == 0:
            raise ValueError(
                'ExecutableLocalEnvoy.start() must be called before you can get the port'
            )
        return self._published_port

    async def start(self):
        command = [
            'envoy',
            '-c',
            self._envoy_config,
            # We need to disable hot restarts in order to run multiple
            # proxies at the same time otherwise they will clash
            # trying to create a domain socket. See
            # https://www.envoyproxy.io/docs/envoy/latest/operations/cli#cmdoption-base-id
            # for more details.
            '--disable-hot-restart',
        ]

        if self._debug_mode:
            command.extend(
                [
                    '--log-level',
                    'debug',
                    '--log-path',
                    '/tmp/envoy.log',
                ]
            )

        self._process = await asyncio.create_subprocess_exec(
            *command,
            stdin=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.STDOUT,
            stdout=asyncio.subprocess.PIPE,
        )
        assert self._process.stdout is not None

        async def _output_logs():

            async def read_stdout():
                assert self._process is not None
                assert self._process.stdout is not None
                while not self._process.stdout.at_eof():
                    yield await self._process.stdout.readline()

            async for line in read_stdout():
                decoded_line = line.decode()

                if self._debug_mode:
                    print(decoded_line)

        self._output_logs_task = asyncio.create_task(_output_logs())

    async def stop(self):
        assert self._process is not None
        try:
            self._process.terminate()
            # Wait for the process to terminate, but don't wait too long.
            try:
                await asyncio.wait_for(self._process.wait(), timeout=5.0)
            except asyncio.TimeoutError:
                # The process still hasn't gracefully terminated. Kill the
                # process. There's no way to ignore that signal, so we can
                # safely do a non-timeout-based `await` for it to finish.
                self._process.kill()
                await self._process.wait()
        except ProcessLookupError:
            # The process already exited. That's fine.
            pass
