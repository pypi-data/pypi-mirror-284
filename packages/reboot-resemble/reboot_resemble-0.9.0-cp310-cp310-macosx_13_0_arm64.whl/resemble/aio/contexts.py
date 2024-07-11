from __future__ import annotations

import asyncio
import dataclasses
import grpc.aio
import json
import sys
import traceback
import uuid
from abc import ABC
from backoff import Backoff
from collections import defaultdict
from contextvars import ContextVar
from enum import Enum
from google.protobuf.message import Message
from resemble.aio.aborted import is_grpc_retryable_exception
from resemble.aio.auth import Auth
from resemble.aio.headers import TRANSACTION_PARTICIPANTS_HEADER, Headers
from resemble.aio.idempotency import IdempotencyManager
from resemble.aio.internals.channel_manager import (
    LegacyGrpcChannel,
    _ChannelManager,
)
from resemble.aio.internals.contextvars import Servicing, _servicing
from resemble.aio.tasks import TaskEffect
from resemble.aio.types import (
    ActorId,
    ApplicationId,
    GrpcMetadata,
    ServiceName,
    StateTypeName,
    service_to_state_type,
)
from resemble.v1alpha1 import react_pb2, react_pb2_grpc, sidecar_pb2
from typing import (
    Awaitable,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Optional,
    Tuple,
    TypeVar,
)

ContextT = TypeVar('ContextT', bound='Context')
ResponseT = TypeVar('ResponseT', bound=Message)


class Participants:
    _participants: defaultdict[ServiceName, set[ActorId]]

    @classmethod
    def from_sidecar(cls, participants: sidecar_pb2.Participants):
        """Constructs an instance from the sidecar protobuf representation."""
        result = cls()
        for (service, actor_ids) in participants.participants.items():
            result.update(service, actor_ids.actor_ids)
        return result

    def to_sidecar(self) -> sidecar_pb2.Participants:
        """Helper to construct the sidecar protobuf representation."""
        return sidecar_pb2.Participants(
            participants={
                service:
                    sidecar_pb2.Participants.ActorIds(
                        actor_ids=list(actor_ids)
                    ) for (service, actor_ids) in self._participants.items()
            },
        )

    def __init__(self):
        self._participants = defaultdict(set)

    def __iter__(self) -> Iterator[Tuple[ServiceName, ActorId]]:
        """Returns an iterator of (service, actor_id) tuples for each
        participant."""
        for service, actor_ids in self._participants.items():
            for actor_id in actor_ids:
                yield (service, actor_id)

    def add(self, service_name: ServiceName, actor_id: ActorId):
        self._participants[service_name].add(actor_id)

    def update(self, service_name: ServiceName, actor_ids: Iterable[ActorId]):
        self._participants[service_name].update(actor_ids)

    def union(self, participants: 'Participants'):
        for (service_name, actor_ids) in participants._participants.items():
            self._participants[service_name].update(actor_ids)

    def to_grpc_metadata(self) -> GrpcMetadata:
        """Helper to encode transaction participants into gRPC metadata.
        """
        return (
            (
                TRANSACTION_PARTICIPANTS_HEADER,
                json.dumps(
                    # Need to convert 'set' into a 'list' for JSON
                    # stringification.
                    {
                        service_name: [actor_id.key for actor_id in actor_ids]
                        for (service_name,
                             actor_ids) in self._participants.items()
                    }
                )
            ),
        )

    @classmethod
    def from_grpc_metadata(cls, metadata: GrpcMetadata) -> 'Participants':
        """Helper to decode transaction participants from gRPC metadata.
        """
        for (key, value) in metadata:
            if key == TRANSACTION_PARTICIPANTS_HEADER:
                participants = cls()
                for (service_name, actor_keys) in json.loads(value).items():
                    participants.update(
                        service_name,
                        [
                            ActorId.from_key(
                                service_to_state_type(
                                    ServiceName(service_name)
                                ),
                                actor_key,
                            ) for actor_key in actor_keys
                        ],
                    )

                return participants

        return cls()


class RetryReactively(Exception):
    """Exception to raise when in a reactive method context and wanting to
    retry the method after state or reader's responses have changed.
    """
    pass


class React:
    """Encapsulates machinery necessary for contexts that are "reactive",
    aka, those that are initiated from calls to `React.Query` and who
    then transform subsequent reader calls into `React.Query` calls
    themselves (for full transitive reactivity).
    """

    class Querier(Generic[ResponseT]):
        """Performs the `React.Query` RPCs.

        Maintains an `asyncio.Task` for every unique request that is
        used (uniqueness is determined via serializing the request).

        Expects a call to `cancel_unused()` to cancel the
        `asyncio.Task`s that are no longer necessary.
        """

        # Service, actor, method we are invoking.
        _service: ServiceName
        _actor_id: ActorId
        _method: str

        # Type of the response we are receiving.
        _response_type: type[ResponseT]

        # Event which indicates that new data has been received and we
        # should re-invoke methods.
        _event: asyncio.Event

        _channel_manager: _ChannelManager

        # Tasks that are calling `React.Query`, keyed by the
        # serialized request.
        _tasks: dict[bytes, asyncio.Task]

        # The gRPC call to `React.Query` that each of our
        # `asyncio.Task`s are making.
        _calls: dict[asyncio.Task, grpc.aio.Call]

        # The latest response or error received from calling
        # `React.Query`, set by our `asyncio.Task`s.
        _responses: dict[asyncio.Task, asyncio.Future[ResponseT]]

        # An event indicating that a response has been used and thus
        # the next response can be retrieved.
        _used_response: dict[asyncio.Task, asyncio.Event]

        # The subset of `_tasks` that's been used since the last call
        # to `cancel_*()`.  Any tasks not in this `set` are considered
        # "unused" for the purposes of `cancel_unused()`.
        _used_tasks: set[asyncio.Task]

        def __init__(
            self,
            *,
            service: ServiceName,
            actor_id: ActorId,
            method: str,
            response_type: type[ResponseT],
            event: asyncio.Event,
            channel_manager: _ChannelManager,
        ):
            self._service = service
            self._actor_id = actor_id
            self._method = method
            self._response_type = response_type
            self._event = event
            self._channel_manager = channel_manager
            self._tasks = dict()
            self._calls = dict()
            self._responses = dict()
            self._used_response = dict()
            self._used_tasks = set()

        async def call(
            self,
            request: Message,
            *,
            metadata: GrpcMetadata,
        ) -> tuple[grpc.aio.Call, asyncio.Future[ResponseT]]:
            serialized_request = request.SerializeToString(deterministic=True)

            task: Optional[asyncio.Task] = self._tasks.get(serialized_request)

            if task is not None:
                self._used_tasks.add(task)

                self._used_response[task].set()

                assert task in self._calls
                assert task in self._responses

                return (self._calls[task], self._responses[task])

            # Need to track whether or not we have received
            # the first response because we don't want to
            # cause an unnecessary reaction (i.e.,
            # re-execution of the user's code) for the first
            # response.
            have_first_response = asyncio.Event()

            async def query():
                task: Optional[asyncio.Task] = asyncio.current_task()

                assert task is not None

                # In the event we receive an error from the call we
                # want to try again because it's possible that we'll
                # get a response if some other state changes, but
                # rather than continuously bombarding the server with
                # requests we exponentially backoff before retrying.
                #
                # TODO(benh): introduce a mechanism where we can
                # actually wait until a new response would be
                # produced, e.g., because we track the state
                # version/clock and only retry calls when the state
                # changes.
                backoff = Backoff(max_backoff_seconds=5)

                while True:
                    channel = self._channel_manager.get_channel_from_service_name(
                        self._service, self._actor_id
                    )

                    call = react_pb2_grpc.ReactStub(channel).Query(
                        react_pb2.QueryRequest(
                            method=self._method,
                            request=serialized_request,
                        ),
                        metadata=metadata,
                    )

                    # We need an extra level of indirection to loop
                    # through the gRPC responses because empirically
                    # it appears as though we cannot cancel an
                    # `asyncio.Task` that is "blocked" in the gRPC
                    # `call` generator.
                    #
                    # By using an extra coroutine we can properly get
                    # interrupted on cancellation and then call
                    # `call.cancel()` which will cancel the underlying
                    # gRPC generator.
                    async def loop():
                        assert task is not None

                        async for query_response in call:
                            if not query_response.HasField('response'):
                                continue

                            response = self._response_type()
                            response.ParseFromString(query_response.response)

                            self._used_response[task].clear()

                            self._calls[task] = call

                            self._responses[task] = asyncio.Future()
                            self._responses[task].set_result(response)

                            if not have_first_response.is_set():
                                have_first_response.set()
                            else:
                                self._event.set()

                            await self._used_response[task].wait()

                    try:
                        await loop()
                    except asyncio.CancelledError:
                        call.cancel()
                        raise
                    except BaseException as exception:
                        if is_grpc_retryable_exception(exception):
                            continue

                        self._used_response[task].clear()

                        self._calls[task] = call

                        self._responses[task] = asyncio.Future()
                        self._responses[task].set_exception(exception)

                        if not have_first_response.is_set():
                            have_first_response.set()
                        else:
                            self._event.set()

                        await self._used_response[task].wait()

                        await backoff()

            task = asyncio.create_task(query())

            self._tasks[serialized_request] = task
            self._used_response[task] = asyncio.Event()
            self._used_tasks.add(task)

            await have_first_response.wait()

            return await self.call(request, metadata=metadata)

        async def cancel_all(self):
            # Mark all tasks as unused and then cancel unused, which
            # will be all of them!
            self._used_tasks = set()
            await self.cancel_unused()

        async def cancel_unused(self):
            tasks = dict()

            for (serialized_request, task) in self._tasks.items():
                if task in self._used_tasks:
                    tasks[serialized_request] = task
                else:
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        pass
                    except:
                        print(
                            'Failed to cancel task invoking `React.Query`',
                            file=sys.stderr,
                        )
                        traceback.print_exc()
                        pass

            self._tasks = tasks
            self._used_tasks = set()

    _channel_manager: _ChannelManager
    _queriers: dict[str, Querier]
    _event: asyncio.Event

    # The "iteration" of dependency updates that we've received,
    # useful for distinguishing whether or not it is safe to wait on
    # `_event` or if it's possible that we've missed an update.
    _iteration: int

    # Lock to ensure that we only increment `_iteration` once for
    # every set of `_event.set()` calls between `_event.wait()`.
    _lock: asyncio.Lock

    def __init__(self, channel_manager: _ChannelManager):
        self._channel_manager = channel_manager
        self._queriers = dict()
        self._event = asyncio.Event()
        self._iteration = 0
        self._lock = asyncio.Lock()

    @property
    def event(self) -> asyncio.Event:
        return self._event

    @property
    def iteration(self) -> int:
        return self._iteration

    async def iterate(self, iteration: int):
        """Helper for waiting only if we're still at the current iteration."""
        if self._iteration == iteration:
            # Using a lock to ensure that even if there are multiple
            # callers to `iterate`, only one of them increments
            # `self._iteration`.
            async with self._lock:
                if self._iteration == iteration:
                    await self._event.wait()
                    self._event.clear()
                    self._iteration += 1
        return self._iteration

    async def call(
        self,
        *,
        service: ServiceName,
        actor_id: ActorId,
        method: str,
        request: Message,
        response_type: type[ResponseT],
        metadata: GrpcMetadata,
    ) -> tuple[grpc.aio.Call, asyncio.Future[ResponseT]]:
        """Performs an RPC by calling `React.Query` instead."""
        # Lookup or create a `Querier` for performing this RPC and
        # then delegate the call to it.
        key = f'{service}.{method}/{actor_id}'

        querier: Optional[React.Querier[ResponseT]] = self._queriers.get(key)

        if querier is None:
            querier = React.Querier(
                service=service,
                actor_id=actor_id,
                method=method,
                response_type=response_type,
                event=self._event,
                channel_manager=self._channel_manager,
            )
            self._queriers[key] = querier

        assert querier is not None
        return await querier.call(request, metadata=metadata)

    async def cancel_unused_queries(self):
        for querier in self._queriers.values():
            await querier.cancel_unused()

    async def cancel_all_queries(self):
        for querier in self._queriers.values():
            await querier.cancel_all()


class EffectValidation(Enum):
    ENABLED = 1
    QUIET = 2
    DISABLED = 3


class EffectValidationRetry(Exception):
    """An exception type which is raised in order to abort and retry transactions
    for the purposes of effect validation."""


class Context(ABC, IdempotencyManager):
    """Common base class for all contexts.

    Contexts holds information relevant to the current call.

    Construction of a Context object is done by the servicer
    middleware. You should never need to construct a Context yourself.
    """
    # Python asyncio context variable that stores the current context.
    _context: ContextVar[Optional[Context]] = ContextVar(
        'Context of the current asyncio context',
        default=None,
    )

    @classmethod
    def get(cls) -> Optional[Context]:
        """Returns context for the current asyncio context, or None."""
        return cls._context.get()

    @classmethod
    def set(cls, context: Context):
        """Sets the context for the current asyncio context."""
        return cls._context.set(context)

    _channel_manager: _ChannelManager
    _headers: Headers

    # `None` unless this context is being used to run a task.
    _task: Optional[TaskEffect]

    # Participants aggregated from all RPCs rooted at the method for
    # which we initially created this context.
    #
    # We use this when a method is executed within a transaction so
    # that we can pass back to the coordinator the precise set of
    # participants.
    participants: Participants

    # Number of outstanding RPCs rooted at the method for which we
    # initially created this context. Incremented whenever an RPC
    # begins, and decremented when it completes (whether successfully
    # or not).
    #
    # We use this when a method is executed within a transaction to
    # ensure that all RPCs complete so that we know we have aggregated
    # all possible participants - this count must reach 0.
    #
    # TODO(benh): consider using this for not just transactions but
    # all methods, or at least making it the default with an option to
    # opt out.
    outstanding_rpcs: int

    # Whether or not the transaction enclosing this context should
    # abort.
    transaction_must_abort: bool

    # Extra machinery for handling reactive contexts. Set when using
    # the `StateManager.reactively()` helper.
    react: Optional[React]

    # Auth specific information as provided by the `TokenVerifier`, if present.
    auth: Optional[Auth]

    # Whether or not this context is being used for a "constructor",
    # i.e., a writer or transaction of an actor that has not yet been
    # constructed.
    _constructor: bool

    # Any tasks scheduled with this context that we need to include as
    # part of the effects.
    _tasks: list[TaskEffect]

    # NOTE: `_colocated_upserts` argument is for internal use only. See
    # usage in the `StateManager` class.
    _colocated_upserts: Optional[list[tuple[str, Optional[bytes]]]]

    def __init__(
        self,
        *,
        channel_manager: _ChannelManager,
        headers: Headers,
        task: Optional[TaskEffect] = None,
    ):
        # Note: this is intended as a private constructor only to be
        # called by the middleware.
        if _servicing.get() is not Servicing.INITIALIZING:
            raise RuntimeError(
                'Context should only be constructed by middleware'
            )

        super().__init__(
            seed=uuid.UUID(bytes=task.task_id.task_uuid)
            if task is not None else None,
            required=isinstance(self, WorkflowContext),
            required_reason=
            'Calls to mutators within a `workflow` must use idempotency'
            if isinstance(self, WorkflowContext) else None,
        )

        self._channel_manager = channel_manager
        self._headers = headers
        self._task = task

        self.participants = Participants()
        self.outstanding_rpcs = 0
        self.transaction_must_abort = False

        self.react = None

        self.auth = None

        self._constructor = False

        self._tasks = []

        self._colocated_upserts = None

        # Store the context as an asyncio contextvar for access via
        # APIs where we don't pass a `context` but we know one has
        # been created (or should have been created).
        Context._context.set(self)

    @property
    def channel_manager(self) -> _ChannelManager:
        """Return channel manager.
        """
        return self._channel_manager

    @property
    def application_id(self) -> ApplicationId:
        """Return application ID.
        """
        assert self._headers.application_id is not None
        return self._headers.application_id

    @property
    def service_name(self) -> ServiceName:
        """Return service name.
        """
        return self._headers.service_name

    @property
    def state_type_name(self) -> StateTypeName:
        """Return the name of the state type.
        """
        return self._headers.state_type_name

    @property
    def actor_id(self) -> ActorId:
        """Return actor id.
        """
        return self._headers.actor_id

    @property
    def transaction_ids(self) -> Optional[list[uuid.UUID]]:
        """Returns all transaction ids that make up the path from root and
        nested transactions to the current transaction.
        """
        return self._headers.transaction_ids

    @property
    def transaction_id(self) -> Optional[uuid.UUID]:
        """Return transaction id.
        """
        if self._headers.transaction_ids is not None:
            return self._headers.transaction_ids[-1]
        else:
            return None

    @property
    def transaction_root_id(self) -> Optional[uuid.UUID]:
        """Return transaction root id, i.e., the outermost transaction.
        """
        if self._headers.transaction_ids is not None:
            return self._headers.transaction_ids[0]
        else:
            return None

    @property
    def transaction_parent_ids(self) -> Optional[list[uuid.UUID]]:
        """Return transaction parent ids if this is a nested transaction.
        """
        if self._headers.transaction_ids is not None:
            return self._headers.transaction_ids[:-1]
        else:
            return None

    @property
    def workflow_id(self) -> Optional[uuid.UUID]:
        """Return workflow id.
        """
        return self._headers.workflow_id

    @property
    def transaction_coordinator_service(self) -> Optional[ServiceName]:
        """Return transaction coordinator service.
        """
        return self._headers.transaction_coordinator_service

    @property
    def transaction_coordinator_state_type(self) -> Optional[StateTypeName]:
        """Return transaction coordinator state type.
        """
        return self._headers.transaction_coordinator_state_type

    @property
    def transaction_coordinator_actor_id(self) -> Optional[ActorId]:
        """Return transaction coordinator actor id.
        """
        return self._headers.transaction_coordinator_actor_id

    @property
    def idempotency_key(self) -> Optional[uuid.UUID]:
        """Return optional idempotency key.
        """
        return self._headers.idempotency_key

    @property
    def bearer_token(self) -> Optional[str]:
        """Return optional bearer token.
        """
        return self._headers.bearer_token

    @property
    def constructor(self) -> bool:
        """Return whether or not this context is being used for a method that
        is acting as a constructor.
        """
        return self._constructor

    @property
    def task(self) -> Optional[TaskEffect]:
        """Returns the task if this context is being used to execute a
        task, otherwise `None`.
        """
        return self._task

    @property
    def task_id(self) -> Optional[uuid.UUID]:
        """Returns the task if this context is being used to execute a
        task, otherwise `None`.
        """
        return (
            uuid.UUID(bytes=self._task.task_id.task_uuid)
            if self._task is not None else None
        )

    @property
    def iteration(self) -> Optional[int]:
        """Returns the loop iteration if this context is being used to
        execute a control loop task, otherwise `None`.

        Note that a single loop iteration may _retry_ multiple times; each of
        these retries are for the same iteration. A new iteration starts only
        when the previous iteration completes by returning `Loop`.
        """
        return self._task.iteration if self._task is not None else None

    def legacy_grpc_channel(self) -> grpc.aio.Channel:
        """Get a gRPC channel that can connect to any Resemble-hosted legacy
        gRPC service. Simply use this channel to create a Stub and call it, no
        address required."""
        return LegacyGrpcChannel(self._channel_manager)


class ReaderContext(Context):
    """Call context for a reader call."""


class WriterContext(Context):
    """Call context for a writer call."""


class TransactionContext(Context):
    """Call context for a transaction call."""

    def __init__(
        self,
        *,
        channel_manager: _ChannelManager,
        headers: Headers,
        task: Optional[TaskEffect] = None,
    ):
        assert (
            headers.transaction_ids is None or len(headers.transaction_ids) > 0
        )

        if headers.transaction_ids is None:
            headers = dataclasses.replace(
                headers,
                transaction_ids=[uuid.uuid4()],
                # The actor servicing the request to executing a
                # method of kind transaction acts as the transaction
                # coordinator.
                transaction_coordinator_service=headers.service_name,
                transaction_coordinator_actor_id=headers.actor_id,
            )
        else:
            assert (
                headers.transaction_coordinator_service is not None and
                headers.transaction_coordinator_actor_id is not None
            )

            headers = dataclasses.replace(
                headers,
                transaction_ids=headers.transaction_ids + [uuid.uuid4()],
            )

        super().__init__(
            channel_manager=channel_manager,
            headers=headers,
            task=task,
        )

    @property
    def transaction_ids(self) -> list[uuid.UUID]:
        """Returns all transaction ids that make up the path from root and
        nested transactions to the current transaction.
        """
        assert self._headers.transaction_ids is not None
        return self._headers.transaction_ids

    @property
    def transaction_id(self) -> uuid.UUID:
        """Return transaction id.
        """
        assert self._headers.transaction_ids is not None
        return self._headers.transaction_ids[-1]

    @property
    def transaction_root_id(self) -> uuid.UUID:
        """Return transaction root id, i.e., the outermost transaction.
        """
        assert self._headers.transaction_ids is not None
        return self._headers.transaction_ids[0]

    @property
    def transaction_parent_ids(self) -> list[uuid.UUID]:
        """Return transaction parent ids if this is a nested transaction.
        """
        assert self._headers.transaction_ids is not None
        return self._headers.transaction_ids[:-1]

    @property
    def transaction_coordinator_service(self) -> ServiceName:
        """Return transaction coordinator service.
        """
        assert self._headers.transaction_coordinator_service is not None
        return self._headers.transaction_coordinator_service

    @property
    def transaction_coordinator_actor_id(self) -> ActorId:
        """Return transaction coordinator actor id.
        """
        assert self._headers.transaction_coordinator_actor_id is not None
        return self._headers.transaction_coordinator_actor_id

    @property
    def nested(self) -> bool:
        """Return whether or not this transaction is nested.
        """
        assert self._headers.transaction_ids is not None
        return len(self._headers.transaction_ids) > 1


class WorkflowContext(Context):
    """Call context for a workflow call."""


async def until(
    context: WorkflowContext,
    condition: Callable[[], Awaitable[bool]],
):
    """Helper for waiting for something within a `WorkflowContext` that
    re-executes the given callable everytime that some reactive state
    has changed instead of raising `RetryReactively` and re-executing
    the entire workflow from the beginning (even though it's safe to
    do so, it is more expensive).
    """
    assert context.react is not None
    iteration = context.react.iteration
    while not await condition():
        iteration = await context.react.iterate(iteration)
