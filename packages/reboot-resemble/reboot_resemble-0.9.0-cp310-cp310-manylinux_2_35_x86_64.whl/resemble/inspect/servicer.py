import asyncio
import google
import grpc
import json
import os
import sys
import traceback
from collections import defaultdict
from google.api.httpbody_pb2 import HttpBody
from google.protobuf.struct_pb2 import Struct
from pathlib import Path
from resemble.aio.internals.channel_manager import _ChannelManager
from resemble.aio.internals.middleware import Middleware
from resemble.aio.placement import PlacementClient
from resemble.aio.state_managers import StateManager
from resemble.aio.types import (
    ActorId,
    ApplicationId,
    ConsensusId,
    ServiceName,
    StateTypeName,
    state_type_to_service,
)
from resemble.v1alpha1.inspect import inspect_pb2_grpc
from resemble.v1alpha1.inspect.inspect_pb2 import (
    GetAllActorsRequest,
    GetAllActorsResponse,
    WebDashboardRequest,
)
from respect.logging import get_logger
from typing import AsyncIterator, Optional

logger = get_logger(__name__)


class InspectServicer(inspect_pb2_grpc.InspectServicer):

    def __init__(
        self,
        application_id: ApplicationId,
        consensus_id: ConsensusId,
        state_manager: StateManager,
        placement_client: PlacementClient,
        channel_manager: _ChannelManager,
        middleware_by_service_name: dict[ServiceName, Middleware],
    ):
        self._application_id = application_id
        self._consensus_id = consensus_id
        self._state_manager = state_manager
        self._placement_client = placement_client
        self._channel_manager = channel_manager
        self._middleware_by_service_name = middleware_by_service_name

    def add_to_server(self, server: grpc.aio.Server) -> None:
        inspect_pb2_grpc.add_InspectServicer_to_server(self, server)

    async def _aggregate_all_actors(
        self,
        grpc_context: grpc.aio.ServicerContext,
        only_consensus_id: ConsensusId,
    ) -> AsyncIterator[GetAllActorsResponse]:

        async def call_other_consensus(
            consensus_id: ConsensusId,
            parts: dict[ConsensusId, google.protobuf.struct_pb2.Struct],
            part_changed: asyncio.Event,
        ):
            """
            Calls `GetAllActors` on the given consensus, and updates its entry
            in `parts` every time a new response is sent.
            """
            channel = self._channel_manager.get_channel_to(
                self._placement_client.address_for_consensus(consensus_id)
            )
            # TODO: Forward admin auth. See #2274.
            stub = inspect_pb2_grpc.InspectStub(channel)
            async for response in stub.GetAllActors(
                request=GetAllActorsRequest(only_consensus_id=consensus_id)
            ):
                parts[consensus_id] = response.actors
                part_changed.set()

        # ASSUMPTION: the list of known consensuses is stable.
        parts: dict[ConsensusId, google.protobuf.struct_pb2.Struct] = {}
        parts_changed = asyncio.Event()

        # In the background, ask all of the consensuses about their part of
        # the total set of actors.
        consensus_ids = self._placement_client.known_consensuses(
            self._application_id
        ) if only_consensus_id == "" else [only_consensus_id]
        tasks = [
            asyncio.create_task(
                call_other_consensus(consensus_id, parts, parts_changed)
            ) for consensus_id in consensus_ids
        ]

        try:
            while True:
                # Every time any of the parts change, recompute the total view of
                # all actors.
                await asyncio.wait(
                    # Also await 'tasks', so we hear if there's a failure
                    # gathering any of the parts.
                    [asyncio.create_task(parts_changed.wait())] + tasks,
                    return_when=asyncio.FIRST_COMPLETED
                )
                # The `tasks` will never finish without an exception, so we know
                # if we're here that a part must have changed.
                parts_changed.clear()

                # Only send an overview once we've heard from all consensuses;
                # we try to avoid sending incomplete results so clients are
                # easier to write.
                if len(parts) < len(consensus_ids):
                    continue

                # Assemble an overview of all actors from the parts.
                result = GetAllActorsResponse()
                for part in parts.values():
                    for service_name, actors in part.items():
                        if service_name not in result.actors:
                            result.actors[service_name] = (
                                google.protobuf.struct_pb2.Struct()
                            )
                        result.actors[service_name].update(actors)
                yield result
        finally:
            for task in tasks:
                if not task.done():
                    task.cancel()
            await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    async def GetAllActors(
        self,
        request: GetAllActorsRequest,
        grpc_context: grpc.aio.ServicerContext,
    ) -> AsyncIterator[GetAllActorsResponse]:
        # TODO: Require admin auth. See #2274.
        # If this call is not specifically for this consensus, act as an
        # aggregator.
        if request.only_consensus_id != self._consensus_id:
            # Act as (only) an aggregator.
            #
            # TODO(rjh): consider limiting the response size (e.g. to top N
            #            actors, with paging?).
            async for response in self._aggregate_all_actors(
                grpc_context, request.only_consensus_id
            ):
                yield response
            return

        # Dictionary representing the state_types and actors that we will
        # convert to JSON.
        state_types_and_actors: defaultdict[StateTypeName,
                                            dict[ActorId,
                                                 object]] = defaultdict(dict)

        # Event indicating that our first loads have all completed, and that we
        # can send a first JSON version of our state over the network. Note that
        # this first load may have touched _no_ actors.
        first_loads_complete = asyncio.Event()

        # Event indicating that our dictionary has changed and we
        # should send another JSON version of it over the network.
        state_types_and_actors_modified = asyncio.Event()

        async def watch_actor(
            state_type: StateTypeName,
            actor_id: ActorId,
            first_load_complete: asyncio.Event,
        ):
            """Helper that watches for state updates on a specific actor."""
            middleware: Optional[Middleware
                                ] = self._middleware_by_service_name.get(
                                    state_type_to_service(state_type)
                                )

            if middleware is None:
                raise ValueError(f"Unknown state type '{state_type}'")

            # For every state update, save a representation of the
            # state that can be converted into JSON.
            async for state in middleware.inspect(actor_id):
                # We convert our message to JSON, and then back to an
                # `object`, so that when we do the final conversion to
                # JSON we'll only have the fields from the initial
                # conversion.
                state_types_and_actors[state_type][actor_id] = json.loads(
                    google.protobuf.json_format.MessageToJson(
                        state,
                        preserving_proto_field_name=True,
                        ensure_ascii=True,
                    )
                )
                state_types_and_actors_modified.set()
                first_load_complete.set()

        async def watch_actors():
            """Helper that watches for updates from the state manager for the set
               of running actors."""
            # Tasks that are running our `watch_actor(...)` helper.
            watch_actor_tasks: defaultdict[StateTypeName, dict[
                ActorId, asyncio.Task]] = defaultdict(dict)

            try:
                async for actors in self._state_manager.actors():
                    # Start watching any actors that we aren't already watching.
                    first_loads: list[asyncio.Event] = []
                    for (state_type, actor_ids) in actors.items():
                        for actor_id in actor_ids:
                            if actor_id not in watch_actor_tasks[state_type]:
                                first_load_complete = asyncio.Event()
                                watch_actor_tasks[state_type][
                                    actor_id] = asyncio.create_task(
                                        watch_actor(
                                            state_type,
                                            actor_id,
                                            first_load_complete,
                                        )
                                    )
                                first_loads.append(first_load_complete)

                    # TODO(benh): stop watching any actors that we are
                    # already watching.
                    for state_type in watch_actor_tasks:
                        for actor_id in watch_actor_tasks[state_type]:
                            if state_type not in actors or actor_id not in actors[
                                state_type]:
                                raise NotImplementedError(
                                    'Removing actors is not yet implemented'
                                )

                    if not first_loads_complete.is_set():
                        await asyncio.gather(*[f.wait() for f in first_loads])
                        first_loads_complete.set()
            finally:
                # Clean up after ourselves and stop watching actors.
                for tasks in watch_actor_tasks.values():
                    for task in tasks.values():
                        task.cancel()

                    await asyncio.wait(
                        tasks.values(),
                        return_when=asyncio.ALL_COMPLETED,
                    )

        watch_actors_task = asyncio.create_task(watch_actors())

        try:
            # Wait for all of the actors that were already known when this call
            # started to be loaded before communicating the first result. That
            # helps ensure that the first response from `Inspect()` is complete,
            # making clients easier to write.
            await first_loads_complete.wait()
            while True:
                state_types_and_actors_modified.clear()
                actors = Struct()
                actors.update(state_types_and_actors)
                yield GetAllActorsResponse(actors=actors)
                await state_types_and_actors_modified.wait()
        finally:
            # Clean up after ourselves and stop watching for new
            # actors (which also will stop watching individual
            # actors).
            try:
                watch_actors_task.cancel()
                await watch_actors_task
            except asyncio.CancelledError:
                pass
            except:
                # Print a stacktrace here but don't bother raising as
                # we don't care about this task any more.
                print(
                    'Failed trying to watch for new/removed actors',
                    file=sys.stderr
                )
                traceback.print_exc()

    async def WebDashboard(
        self,
        request: WebDashboardRequest,
        grpc_context: grpc.aio.ServicerContext,
    ) -> HttpBody:
        file = request.file or 'index.html'

        CONTENT_TYPE_BY_FILE = {
            'index.html': 'text/html',
            'bundle.js': 'text/javascript',
            'bundle.js.map': 'application/json',
        }
        if file not in CONTENT_TYPE_BY_FILE:
            logger.warning(f"Request for unexpected file: '{file}'")
            await grpc_context.abort(grpc.StatusCode.NOT_FOUND)
            raise RuntimeError('This code is unreachable')

        path = Path(os.path.join(os.path.dirname(__file__), file))
        return HttpBody(
            content_type=f'{CONTENT_TYPE_BY_FILE[file]}; charset=utf-8',
            data=path.read_text().encode('utf-8'),
        )
