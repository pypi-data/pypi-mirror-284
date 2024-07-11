import grpc
from google.protobuf import any_pb2
from resemble.aio.internals.channel_manager import _ChannelManager
from resemble.aio.internals.tasks_cache import TasksCache
from resemble.aio.placement import PlacementClient
from resemble.aio.state_managers import StateManager
from resemble.aio.types import (
    ApplicationId,
    ConsensusId,
    StateTypeName,
    state_type_to_service,
)
from resemble.consensus.sidecar import NonexistentTaskId
from resemble.v1alpha1 import tasks_pb2, tasks_pb2_grpc
from typing import Optional


class TasksServicer(tasks_pb2_grpc.TasksServicer):

    def __init__(
        self,
        state_manager: StateManager,
        cache: TasksCache,
        placement_client: PlacementClient,
        channel_manager: _ChannelManager,
        application_id: ApplicationId,
        consensus_id: ConsensusId,
    ):
        self._cache = cache
        self._state_manager = state_manager
        self._placement_client = placement_client
        self._channel_manager = channel_manager
        self._application_id = application_id
        self._consensus_id = consensus_id

    def add_to_server(self, server: grpc.aio.Server) -> None:
        tasks_pb2_grpc.add_TasksServicer_to_server(self, server)

    async def Wait(
        self,
        request: tasks_pb2.WaitRequest,
        grpc_context: grpc.aio.ServicerContext,
    ) -> tasks_pb2.WaitResponse:
        """Implementation of Tasks.Wait()."""
        # Determine whether this is the right consensus to serve this request.
        authoritative_consensus = self._placement_client.consensus_for_actor(
            self._application_id,
            state_type_to_service(StateTypeName(request.task_id.state_type)),
            request.task_id.actor_id,
        )
        if authoritative_consensus != self._consensus_id:
            # This is NOT the correct consensus. Forward to the correct one.
            correct_address = self._placement_client.address_for_consensus(
                authoritative_consensus
            )
            channel = self._channel_manager.get_channel_to(correct_address)
            stub = tasks_pb2_grpc.TasksStub(channel)
            return await stub.Wait(
                metadata=grpc_context.invocation_metadata(),
                request=request,
            )

        cached_response = await self._cache.get(request.task_id)

        if cached_response is not None:
            any_response = any_pb2.Any()
            any_response.ParseFromString(cached_response)
            return tasks_pb2.WaitResponse(response=any_response)

        # Task is not cached; try and load it via the state manager.
        try:
            response: Optional[bytes] = (
                await self._state_manager.load_task_response(request.task_id)
            )
        except NonexistentTaskId:
            await grpc_context.abort(code=grpc.StatusCode.NOT_FOUND)
        else:
            # Invariant: 'response' must not be 'None'.
            #
            # Explanation: For an unknown task_id,
            # load_task_response() will raise, so to get here, task_id
            # must belong to a valid, but evicted, task. We only evict
            # tasks from our cache if they have completed, and
            # completed tasks are required to have a response stored
            # (although that response may itself be empty).
            assert response is not None

            # Cache the task response for temporal locality.
            self._cache.put_with_response(request.task_id, response)

            any_response = any_pb2.Any()
            any_response.ParseFromString(response)

            return tasks_pb2.WaitResponse(response=any_response)

    async def ListPendingTasks(
        self, _request: tasks_pb2.ListPendingTasksRequest,
        grpc_context: grpc.aio.ServicerContext
    ) -> tasks_pb2.ListPendingTasksResponse:
        """Implementation of Tasks.ListPendingTasks()."""
        return tasks_pb2.ListPendingTasksResponse(
            task_ids=self._cache.get_pending_tasks()
        )
