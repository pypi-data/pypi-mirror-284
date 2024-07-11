import uuid
from contextlib import contextmanager
from dataclasses import dataclass
from google.protobuf.message import Message
from resemble.aio.types import ActorId, GrpcMetadata, ServiceName
from typing import Iterator, Optional


class Idempotency:
    """Describes how to perform a mutation idempotently, either by using a
    human readable alias, e.g., 'Charge credit card', and letting the
    system generate a key, or by explicitly providing the key.
    """

    def __init__(
        self,
        *,
        alias: Optional[str] = None,
        key: Optional[str] = None,
        generate: bool = False,
    ):
        """Constructs an idempotency instance. Only one of 'alias' or 'key'
        should be specified if `generate` is `False`, otherwise
        neither should be specified.

        :param alias: human readable alias, e.g., 'Charge credit
        card', that _must_ be unique within the lifetime of the
        current 'Context' or 'Workflow'.

        :param key: idempotency key, e.g., stringified version of a
        UUID.

        :param generate: whether or not to generate idempotency, e.g.,
        from an empty `.idempotently()`.
        """
        assert (
            (alias is None and key is None and generate) or
            (alias is not None and key is None and not generate) or
            (alias is None and key is not None and not generate)
        )
        self._alias = alias
        self._key = key
        self._generate = generate

    @property
    def alias(self) -> Optional[str]:
        """Returns the alias or None."""
        return self._alias

    @property
    def key(self) -> Optional[str]:
        """Returns the key or None."""
        return self._key

    @property
    def generate(self) -> bool:
        """Returns whether or not to generate idempotency."""
        return self._generate


class IdempotencyManager:

    @dataclass(kw_only=True)
    class Mutation:
        # Identifiers of the mutation being performed.
        service: ServiceName
        actor_id: ActorId

        # Method name, or none if this is for an inline writer.
        method: Optional[str]

        # Request of the mutation being performed, or none if this is
        # for an inline writer.
        request: Optional[Message]

        # Serialized request of the mutation being performed
        # (optionally, lazily computed in the event it is never
        # necessary so we don't always pay for serialization).
        serialized_request: Optional[bytes]

        # Metadata of the mutation being performed.
        metadata: Optional[GrpcMetadata]

        # Whether or not idempotency for this mutation was generated.
        idempotency_generated: bool

    # Map from (service, actor, alias) to a generated UUID for an
    # idempotency key.
    _aliases: dict[tuple[ServiceName, ActorId, str], uuid.UUID]

    # Map from idempotency key to its mutation.
    _mutations: dict[str, Mutation]

    # We need to track whether or not any RPCs without idempotency
    # have been made so that we know whether or not to toggle
    # uncertainty if a mutation fails. Not that the mutation that
    # fails might in fact be an idempotent mutation, but attempting to
    # perform a mutation without idempotency _after_ a mutation has
    # failed may be due to a user doing a manual retry which may cause
    # an additional undesired mutation.
    _rpcs_without_idempotency: bool

    # Whether or not a mutation's success or failure is uncertain.
    _uncertain_mutation: bool

    # The service, actor_id, and method of the mutation that is uncertain.
    _uncertain_mutation_service: Optional[ServiceName]
    _uncertain_mutation_actor_id: Optional[ActorId]
    _uncertain_mutation_method: Optional[str]

    def __init__(
        self,
        *,
        seed: Optional[uuid.UUID] = None,
        required: bool = False,
        required_reason: Optional[str] = None,
    ):
        self._seed = seed

        self._required = required
        self._required_reason = required_reason

        assert (
            (not self._required and self._required_reason is None) or
            (self._required and self._required_reason is not None)
        )

        self.reset()

    def reset(self):
        self._aliases = {}
        self._mutations = {}
        self._rpcs_without_idempotency = False
        self._uncertain_mutation = False
        self._uncertain_mutation_service = None
        self._uncertain_mutation_actor_id = None
        self._uncertain_mutation_method = None

    @contextmanager
    def idempotently(
        self,
        *,
        service: ServiceName,
        actor_id: ActorId,
        method: Optional[str],
        request: Optional[Message],
        metadata: Optional[GrpcMetadata],
        idempotency: Optional[Idempotency],
    ) -> Iterator[Optional[str]]:
        """Ensures that either all mutations are performed idempotently or
        raises in the face of uncertainty about a mutation to avoid a
        possible undesired mutation."""
        if idempotency is None:
            if self._required:
                assert self._required_reason is not None
                raise RuntimeError(self._required_reason)

            self._rpcs_without_idempotency = True

        if self._uncertain_mutation:
            assert self._uncertain_mutation_service is not None
            uncertain_mutation_name = self._mutation_name(
                self._uncertain_mutation_service,
                self._uncertain_mutation_method,
            )
            raise RuntimeError(
                "Because we don't know if the mutation from calling "
                f"{uncertain_mutation_name} of actor "
                f"'{self._uncertain_mutation_actor_id}' failed or "
                "succeeded AND you've made some NON-IDEMPOTENT RPCs we can't "
                "reliably determine whether or not the call to "
                f"{self._mutation_name(service, method)} of actor "
                f"'{actor_id}' is due to a retry which may cause an undesired "
                "mutation -- if you are trying to write your own manual retry "
                "logic you should ensure you're always using an idempotency "
                "alias (or passing an explicit idempotency key) for mutations"
            )

        try:
            if idempotency is not None:
                yield self._idempotency_key_from(
                    service=service,
                    actor_id=actor_id,
                    method=method,
                    request=request,
                    metadata=metadata,
                    idempotency=idempotency,
                )
            else:
                yield None
        # TODO(benh): differentiate errors so that we only set
        # uncertainty when we are truly uncertain.
        except:
            # The `yield` threw an exception, which means the user
            # code that we're wrapping (an RPC to a mutation on
            # `service`) failed. We're uncertain whether that mutation
            # succeeded or failed (there are many ways exceptions can
            # get thrown, and not all errors can be clear on whether
            # the RPC has definitively failed on the server).
            #
            # We want to set uncertainty regardless of whether or not
            # _this_ call has an idempotency key because a user might
            # manually _retry_ another call that did not have an
            # idempotency key and accidentally perform a mutation more
            # than once.
            if self._rpcs_without_idempotency:
                assert not self._uncertain_mutation
                self._uncertain_mutation = True
                self._uncertain_mutation_service = service
                self._uncertain_mutation_actor_id = actor_id
                self._uncertain_mutation_method = method
            raise

    def acknowledge_idempotency_uncertainty(self):
        assert self._uncertain_mutation
        self._uncertain_mutation = False
        self._uncertain_mutation_service = None
        self._uncertain_mutation_actor_id = None
        self._uncertain_mutation_method = None

    def _mutation_name(
        self,
        service: ServiceName,
        method: Optional[str],
    ):
        if method is None:
            return f"inline writer of '{service}'"
        else:
            return f"'{service}.{method}'"

    def _idempotency_key_from(
        self,
        *,
        service: ServiceName,
        actor_id: ActorId,
        method: Optional[str],
        request: Optional[Message],
        metadata: Optional[GrpcMetadata],
        idempotency: Idempotency,
    ) -> str:
        idempotency_key = self._get_or_create_idempotency_key(
            service, actor_id, method, idempotency
        )

        if idempotency_key not in self._mutations:
            self._mutations[idempotency_key] = IdempotencyManager.Mutation(
                service=service,
                actor_id=actor_id,
                method=method,
                request=request,
                serialized_request=None,
                metadata=metadata,
                idempotency_generated=idempotency.generate,
            )
            return idempotency_key

        mutation = self._mutations[idempotency_key]

        # If we're seeing a mutation that maps to this idempotency key
        # _again_ and the idempotency was generated that means someone
        # has made more than one empty `.idempotently()` and we need
        # to error out asking them to explicitly use an idempotency
        # alias or key.
        if mutation.idempotency_generated:
            raise ValueError(
                f"To call {self._mutation_name(service, method)} of '{actor_id}' "
                "more than once within a context (or `Workflow`), an idempotency "
                "alias or key must be specified"
            )

        if (
            mutation.service != service or mutation.actor_id != actor_id or
            mutation.method != method
        ):
            raise ValueError(
                f"Idempotency key for {self._mutation_name(service, method)} "
                f"of actor '{actor_id}' is being reused _unsafely_; you can "
                "not reuse an idempotency key that was previously used for "
                f"{self._mutation_name(mutation.service, mutation.method)} "
                f"of actor '{mutation.actor_id}'"
            )

        if (
            (mutation.request is None and request is not None) or
            (mutation.request is not None and request is None)
        ):
            raise ValueError(
                f"Idempotency key for {self._mutation_name(service, method)} "
                f"of actor '{actor_id}' is being reused _unsafely_; you can "
                "not reuse an idempotency key with a different request"
            )
        elif mutation.request is not None:
            assert request is not None

            if mutation.serialized_request is None:
                mutation.serialized_request = mutation.request.SerializeToString(
                    deterministic=True,
                )

            if mutation.serialized_request != request.SerializeToString(
                deterministic=True,
            ):
                raise ValueError(
                    f"Idempotency key for {self._mutation_name(service, method)} "
                    f"of actor '{actor_id}' is being reused _unsafely_; you can "
                    "not reuse an idempotency key with a different request"
                )

        if mutation.metadata != metadata:
            raise ValueError(
                f"Idempotency key for {self._mutation_name(service, method)} "
                f"of actor '{actor_id}' is being reused _unsafely_; you can "
                "not reuse an idempotency key with different metadata"
            )

        return idempotency_key

    def _get_or_create_idempotency_key(
        self,
        service: ServiceName,
        actor_id: ActorId,
        method: Optional[str],
        idempotency: Idempotency,
    ) -> str:
        if idempotency.key is not None:
            return idempotency.key

        alias: str

        if idempotency.generate:
            alias = f'{self._mutation_name(service, method)}@{actor_id}'
        else:
            assert idempotency.alias is not None
            alias = idempotency.alias

        assert alias is not None

        key = (service, actor_id, alias)

        if key not in self._aliases:
            if self._seed is None:
                self._aliases[key] = uuid.uuid4()
            else:
                # A version 5 UUID is a deterministic hash from a
                # "seed" UUID and some data (bytes or string, in our
                # case the string `alias`).
                self._aliases[key] = uuid.uuid5(self._seed, alias)

        return str(self._aliases[key])
