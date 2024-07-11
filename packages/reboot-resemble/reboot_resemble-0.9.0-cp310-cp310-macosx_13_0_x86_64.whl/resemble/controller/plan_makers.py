import math
import time
from resemble.aio.servers import _ServiceServer
from resemble.controller.application_config import ApplicationConfig
from resemble.controller.exceptions import InputError
from resemble.v1alpha1 import placement_planner_pb2
from respect.logging import get_logger
from typing import Iterable, Optional

logger = get_logger(__name__)

# The default number of replicas must remain 1, to remain backwards compatible
# with existing applications - adding more consensuses is a breaking change.
DEFAULT_NUM_REPLICAS = 1


def _shard_first_keys(num_replicas: int) -> list[bytes]:
    NUM_BYTE_VALUES = 256
    if num_replicas > NUM_BYTE_VALUES:
        raise InputError(
            f"'ApplicationConfig.spec.replicas' must be less than or equal to "
            f"{NUM_BYTE_VALUES}; got {num_replicas}."
        )
    if not math.log2(num_replicas).is_integer():
        raise InputError(
            f"'ApplicationConfig.spec.replicas' must be a power of 2; got {num_replicas}."
        )
    shard_size = NUM_BYTE_VALUES // num_replicas
    # The first shard always begins at the very beginning of the key range.
    return [b""] + [bytes([i * shard_size]) for i in range(1, num_replicas)]


def make_consensus_id(
    application_id: str, consensus_index: int, num_consensuses: int
) -> str:
    """
    Generates a consensus ID for a consensus with a given index.
    """
    # For backwards compatibility, if we have only a single consensus that
    # consensus is named after the application without any index.
    if num_consensuses == 1:
        return application_id

    # For forwards compatibility we'll use a 6-digit zero-padded index in
    # consensus names. That allows us to have up to 1 million consensuses per
    # application, which is probably enough.
    return f"{application_id}-c{consensus_index:06d}"


class PlanMaker:
    """
    Logic to construct a placement Plan based on a set of currently valid
    ApplicationConfigs. Designed to be extendable for different Plan structures.
    """

    last_version: Optional[int] = None

    def make_plan(
        self,
        application_configs: Iterable[ApplicationConfig],
    ) -> placement_planner_pb2.Plan:
        """
        Construct a Plan for consensuses that will serve the given list of
        ApplicationConfigs.
        """
        applications: list[placement_planner_pb2.Plan.Application] = []
        for application_config in application_configs:
            application_id = application_config.application_id()
            num_replicas = (
                application_config.spec.replicas
                if application_config.spec.HasField('replicas') else
                DEFAULT_NUM_REPLICAS
            )

            # NOTE: We are deliberately using a `list` here instead of a `set`
            # to avoid issues with change of ordering. Some tests rely on the
            # ordering and `set` order elements internally by hash value, which
            # is not stable between platforms.
            unique_service_names: list[str] = []
            for service_name in application_config.spec.service_names:
                if service_name in unique_service_names:
                    logger.warning(
                        "Service name '%s' is duplicated in application '%s'",
                        service_name,
                        application_id,
                    )
                    continue
                # Ignore system services which exist on every consensus.
                if service_name in _ServiceServer.SYSTEM_SERVICE_NAMES:
                    continue
                unique_service_names.append(service_name)

            # One consensus per shard.
            applications.append(
                placement_planner_pb2.Plan.Application(
                    id=application_id,
                    services=[
                        placement_planner_pb2.Plan.Application.Service(
                            name=name
                        ) for name in unique_service_names
                    ],
                    # We'll only have one shard for t
                    # he whole application.
                    shards=[
                        placement_planner_pb2.Plan.Application.Shard(
                            # The ID must be unique across all shards in the
                            # system, so we prefix it with the application ID.
                            # By using a shard index suffix with 9 digits we can
                            # have up to 1 billion shards per application, which
                            # should be a comfortable overkill.
                            id=f"{application_id}-s{shard_index:09d}",
                            consensus_id=make_consensus_id(
                                application_id=application_id,
                                # For now we'll just have one consensus per shard.
                                consensus_index=shard_index,
                                num_consensuses=num_replicas
                            ),
                            range=placement_planner_pb2.Plan.Application.Shard.
                            KeyRange(first_key=shard_first_key),
                        ) for shard_index, shard_first_key in
                        enumerate(_shard_first_keys(num_replicas))
                    ]
                )
            )

        return placement_planner_pb2.Plan(
            version=self.get_version(),
            applications=applications,
        )

    def get_version(self) -> int:
        """
        Return a valid version number that is (expected to be) greater than
        whatever was previously returned or used.
        We use a timestamp (in ns from epoch) to ensure that version numbers
        increase, and further verify that time has not somehow gone backwards.
        """
        timestamp = time.time_ns()
        if self.last_version is not None and timestamp <= self.last_version:
            raise RuntimeError(
                f'Time is not moving forward as expected! '
                f'New timestamp {timestamp} is not after '
                f'old timestamp {self.last_version}.'
            )
        self.last_version = timestamp
        return timestamp
