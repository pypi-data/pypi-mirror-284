import asyncio
import grpc
import json
from asyncio import Queue
from google.protobuf import json_format
from google.protobuf.message import Message
from resemble.aio.internals.channel_manager import _ChannelManager
from resemble.aio.placement import PlacementClient
from resemble.aio.state_managers import StateManager
from resemble.aio.types import (
    ActorId,
    ApplicationId,
    ConsensusId,
    StateTypeName,
    state_type_to_service,
)
from resemble.v1alpha1.admin import exim_pb2, exim_pb2_grpc
from resemble.v1alpha1.admin.exim_pb2 import (
    ExportRequest,
    ExportResponse,
    ImportRequest,
    ImportResponse,
    ListConsensusesRequest,
    ListConsensusesResponse,
)
from typing import AsyncIterator, Optional


class EximServicer(exim_pb2_grpc.EximServicer):

    def __init__(
        self,
        application_id: ApplicationId,
        consensus_id: ConsensusId,
        state_manager: StateManager,
        placement_client: PlacementClient,
        channel_manager: _ChannelManager,
        state_types_by_name: dict[StateTypeName, type[Message]],
    ):
        self._application_id = application_id
        self._consensus_id = consensus_id
        self._state_manager = state_manager
        self._placement_client = placement_client
        self._channel_manager = channel_manager
        self._state_types_by_name = state_types_by_name

    def add_to_server(self, server: grpc.aio.Server) -> None:
        exim_pb2_grpc.add_EximServicer_to_server(self, server)

    async def ListConsensuses(
        self,
        request: ListConsensusesRequest,
        grpc_context: grpc.aio.ServicerContext,
    ) -> ListConsensusesResponse:
        # TODO: Require admin auth. See #2274.
        return ListConsensusesResponse(
            consensus_ids=self._placement_client.known_consensuses(
                self._application_id
            ),
        )

    async def Export(
        self,
        request: ExportRequest,
        grpc_context: grpc.aio.ServicerContext,
    ) -> AsyncIterator[ExportResponse]:
        # TODO: Require admin auth. See #2274.
        if request.consensus_id != self._consensus_id:
            await grpc_context.abort(
                grpc.StatusCode.NOT_FOUND,
                "This process does not host that consensus.",
            )
            raise RuntimeError('This code is unreachable')
        for state_type_name, state_type in self._state_types_by_name.items():
            state = state_type()
            async for actor_id, state_bytes in self._state_manager.export_states(
                state_type_name
            ):
                state.ParseFromString(state_bytes)
                yield ExportResponse(
                    actor_id=exim_pb2.ActorId(
                        state_type=state_type_name,
                        actor_id=actor_id,
                    ),
                    state_json=json.dumps(
                        json_format.MessageToDict(
                            state,
                            preserving_proto_field_name=True,
                        )
                    ).encode()
                )

    async def Import(
        self,
        requests: AsyncIterator[ImportRequest],
        grpc_context: grpc.aio.ServicerContext,
    ) -> ImportResponse:
        # TODO: Require admin auth. See #2274.

        tasks = []
        queues_by_consensus: dict[ConsensusId,
                                  Queue[Optional[ImportRequest]]] = {}

        async def _local_iterator(
            requests: Queue[Optional[ImportRequest]],
        ) -> AsyncIterator[tuple[StateTypeName, ActorId, Message]]:
            while True:
                request = await requests.get()
                if request is None:
                    return

                state_type_name = StateTypeName(request.actor_id.state_type)
                message_type = self._state_types_by_name.get(state_type_name)
                if message_type is None:
                    raise ValueError(
                        "Unrecognized state type: {request.actor_id.state_type!r}"
                    )
                yield (
                    state_type_name,
                    request.actor_id.actor_id,
                    json_format.Parse(
                        request.state_json,
                        message_type(),
                        ignore_unknown_fields=False,
                    ),
                )

        async def _remote_iterator(
            requests: Queue[Optional[ImportRequest]],
        ) -> AsyncIterator[ImportRequest]:
            while True:
                request = await requests.get()
                if request is None:
                    return
                yield request

        async def _task(
            consensus_id: ConsensusId,
            states: Queue[Optional[ImportRequest]],
        ) -> None:
            if consensus_id == self._consensus_id:
                await self._state_manager.import_states(
                    _local_iterator(states)
                )
            else:
                channel = self._channel_manager.get_channel_to(
                    self._placement_client.address_for_consensus(consensus_id)
                )
                # TODO: Forward admin auth. See #2274.
                exim = exim_pb2_grpc.EximStub(channel)
                await exim.Import(_remote_iterator(states))

        # Route each request to a per-consensus Queue, with a Task that will drain it
        # to the appropriate destination.
        async for request in requests:
            consensus_id = self._placement_client.consensus_for_actor(
                self._application_id,
                state_type_to_service(
                    StateTypeName(request.actor_id.state_type)
                ),
                request.actor_id.actor_id,
            )
            queue = queues_by_consensus.get(consensus_id)
            if queue is None:
                queue = Queue(maxsize=128)
                queues_by_consensus[consensus_id] = queue
                tasks.append(asyncio.create_task(_task(consensus_id, queue)))

            await queue.put(request)

        # And a sentinel value to each queue, and gather the tasks to wait for
        # them to flush to their destinations.
        await asyncio.gather(
            *(queue.put(None) for queue in queues_by_consensus.values()),
        )
        await asyncio.gather(*tasks)

        return ImportResponse()
