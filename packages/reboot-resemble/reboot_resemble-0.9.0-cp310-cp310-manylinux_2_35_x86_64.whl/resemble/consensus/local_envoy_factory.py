import os
from resemble.aio.servicers import Routable
from resemble.consensus.docker_local_envoy import DockerLocalEnvoy
from resemble.consensus.executable_local_envoy import ExecutableLocalEnvoy
from resemble.consensus.local_envoy import LocalEnvoy
from resemble.helpers import (
    base64_serialize_proto_descriptor_set,
    generate_proto_descriptor_set,
)
from resemble.settings import (
    ENVVAR_LOCAL_ENVOY_MODE,
    ENVVAR_LOCAL_ENVOY_TLS_CERTIFICATE_PATH,
    ENVVAR_LOCAL_ENVOY_TLS_KEY_PATH,
    ENVVAR_LOCAL_ENVOY_USE_TLS,
)

RESEMBLE_LOCAL_ENVOY_DEBUG: bool = os.environ.get(
    'RESEMBLE_LOCAL_ENVOY_DEBUG',
    'false',
).lower() == 'true'


class LocalEnvoyFactory:

    @staticmethod
    def create(
        *,
        published_port: int,
        consensus_ports: list[int],
        websocket_ports: list[int],
        application_id: str,
        routables: list[Routable],
    ) -> LocalEnvoy:
        proto_descriptor_set = generate_proto_descriptor_set(routables)

        base64_encoded_proto_desc_set = base64_serialize_proto_descriptor_set(
            proto_descriptor_set
        )

        use_tls = os.environ.get(ENVVAR_LOCAL_ENVOY_USE_TLS) == "True"

        certificate = os.environ.get(
            ENVVAR_LOCAL_ENVOY_TLS_CERTIFICATE_PATH, None
        )
        key = os.environ.get(ENVVAR_LOCAL_ENVOY_TLS_KEY_PATH, None)

        assert certificate is None or key is not None

        if os.environ.get(ENVVAR_LOCAL_ENVOY_MODE) == 'docker':
            return DockerLocalEnvoy(
                published_port=published_port,
                consensus_ports=consensus_ports,
                websocket_ports=websocket_ports,
                application_id=application_id,
                routables=routables,
                base64_encoded_proto_desc_set=base64_encoded_proto_desc_set,
                use_tls=use_tls,
                certificate=certificate,
                key=key,
                debug_mode=RESEMBLE_LOCAL_ENVOY_DEBUG,
            )

        return ExecutableLocalEnvoy(
            published_port=published_port,
            consensus_ports=consensus_ports,
            websocket_ports=websocket_ports,
            application_id=application_id,
            routables=routables,
            base64_encoded_proto_desc_set=base64_encoded_proto_desc_set,
            use_tls=use_tls,
            certificate=certificate,
            key=key,
            debug_mode=RESEMBLE_LOCAL_ENVOY_DEBUG,
        )
