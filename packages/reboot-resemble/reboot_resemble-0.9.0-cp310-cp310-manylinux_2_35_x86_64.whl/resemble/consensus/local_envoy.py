from __future__ import annotations

import os
from jinja2 import Environment, FileSystemLoader
from resemble.aio.types import ServiceName

LOCALHOST_DIRECT_CRT = os.path.join(
    os.path.dirname(__file__), 'localhost.direct.crt'
)

# We open an admin port for Envoy to facilitate debugging. We pick 9901 since
# it's a typical choice (AWS uses it) that's similar to the ports Resemble
# already uses.
ENVOY_ADMIN_PORT = 9901

ENVOY_CONFIG_TEMPLATE_NAME = 'local_envoy_config.yaml.j2'

if not os.path.isfile(LOCALHOST_DIRECT_CRT):
    raise FileNotFoundError(
        "Expecting 'localhost.direct.crt' at path "
        f"'{LOCALHOST_DIRECT_CRT}'"
    )

LOCALHOST_DIRECT_KEY = os.path.join(
    os.path.dirname(__file__), 'localhost.direct.key'
)

if not os.path.isfile(LOCALHOST_DIRECT_KEY):
    raise FileNotFoundError(
        "Expecting 'localhost.direct.key' at path "
        f"'{LOCALHOST_DIRECT_KEY}'"
    )


class LocalEnvoy:
    """
    Wrapper class for setting up a local Envoy outside of Kubernetes. This
    runs Envoy in a Docker container, not in process.

    The user of this class is responsible for calling .start() and .stop().

    Args:
        - consensus_ports: the ports of the Resemble Consensuses that Envoy
          proxies to. Envoy will randomly load-balance between these ports.
        - websocket_ports: the ports on which Resemble accepts websocket
          connections. Envoy will randomly load-balance between these ports.
        - routables: the routable gRPC services to proxy.
        - published_port: the port where Envoy will be reachable by the host
                          machine, forwarded to the Envoy container. We assume
                          only 2 cases for 'published_port':
                          A) '0': we don't know the port yet and we'll have to
                             ask Docker later
                          B) 2. non-'0': we know the port, we'll set it
                             explicitly and forward it to the Envoy container.

    Sample use:
        envoy = LocalEnvoyFactory.create(
            published_port=9991, application_id="my-app",
            consensus_ports=[5001], websocket_ports=[5002],
            routables=[MyGreeterServicer]
        )
        await envoy.start()
        await envoy.stop()
    """

    @property
    def port(self) -> int:
        raise NotImplementedError

    async def start(self) -> None:
        raise NotImplementedError

    async def stop(self) -> None:
        raise NotImplementedError

    @staticmethod
    def _generate_envoy_yaml(
        *,
        proxied_server_host: str,
        envoy_port: int,
        consensus_ports: list[int],
        websocket_ports: list[int],
        application_id: str,
        service_names: list[ServiceName],
        proto_descriptor_bin: bytes,
        template_path: str,
        use_tls: bool,
        tls_certificate_path: str,
        tls_key_path: str,
    ) -> str:
        """
        Loads an Envoy config Jinja template, fills its values and returns a
        yaml string.
        """
        # Inject the Lua filter that handles "mangled" HTTP paths that
        # need to be translated into something that can be routed.
        mangled_http_path_filter_path = os.path.join(
            os.path.dirname(__file__),
            '..',
            'controller',
            'mangled_http_path_filter.lua',
        )

        with open(
            mangled_http_path_filter_path, 'r'
        ) as mangled_http_path_filter_file:
            mangled_http_path_filter = mangled_http_path_filter_file.read()

        template_input = {
            'proxied_server_host': proxied_server_host,
            'envoy_port': envoy_port,
            'consensus_ports': consensus_ports,
            'websocket_ports': websocket_ports,
            'application_id': application_id,
            'service_names': service_names,
            # We have to turn the base64 encoded proto descriptor into a string
            # using .decode() because Jinja can only handle str types.
            'proto_descriptor_bin': proto_descriptor_bin.decode(),
            'envoy_admin_port': ENVOY_ADMIN_PORT,
            'use_tls': use_tls,
            'tls_certificate_path': tls_certificate_path,
            'tls_key_path': tls_key_path,
            'mangled_http_path_filter': mangled_http_path_filter,
        }

        # Define a Jinja2 environment to allow Jinja 'include' find the template
        # file later.
        env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__))),
        )

        template = env.get_template(template_path)

        return template.render(template_input)
