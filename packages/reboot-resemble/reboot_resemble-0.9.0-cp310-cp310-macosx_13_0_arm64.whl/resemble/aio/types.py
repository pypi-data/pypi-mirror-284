from __future__ import annotations

import base64
import hashlib
from resemble.settings import MAX_ACTOR_ID_LENGTH
from typing import Any, NewType, Optional, TypeAlias

# Collection of types used throughout our code with more meaningful names than
# the underlying python types.

ActorKey: TypeAlias = str
ApplicationId = str
ServiceName = NewType("ServiceName", str)
StateTypeName = NewType("StateTypeName", str)
ShardId = str
PartitionId = str
ConsensusId = str
GrpcMetadata = tuple[tuple[str, str], ...]
RoutableAddress = str
KubernetesNamespace = str


class ActorId(str):
    """An ActorId is the globally unique id of a state machine, and acts as the
    partitioning key to assign state machines to consensuses.

    An ActorId is a `/`-separated compound key, with `\` disallowed (because it
    is used to encode `/` in a way that is simple to decode).

    Each key in the ActorId is tagged with a hash of its type, to prevent
    collisions between keys when actors are colocated. See `_state_type_tag`.

    An example actor id for a `com.example.Parent` named `parent`, with a
    colocated `com.example.Child` named `child` is:
      `AEyp_5wmAiADZg:parent/AAcExYZDHb-mAw:child`

    An actor id may also be specified (in a limited number of locations, for
    efficiency) using human readable state names:
      `com.example.Parent:parent/com.example.Child:child`
    """

    @classmethod
    def is_actor_id(cls, candidate: str) -> bool:
        if not isinstance(candidate, str):
            return False
        last_key_start_idx = candidate.rfind('/') + 1
        state_tag_end = last_key_start_idx + _STATE_TYPE_TAG_LENGTH
        if (
            len(candidate) < state_tag_end + 1 or
            candidate[state_tag_end] != ':'
        ):
            return False
        state_type_tag_str = candidate[last_key_start_idx:state_tag_end] + '=='
        try:
            state_type_tag = base64.urlsafe_b64decode(
                state_type_tag_str.encode()
            )
        except Exception:
            return False
        return state_type_tag[0] == 0

    @classmethod
    def from_maybe_readable(cls, candidate: str) -> ActorId:
        if cls.is_actor_id(candidate):
            return ActorId(candidate)
        result = []
        for component in candidate.split('/'):
            component_pieces = component.split(':', maxsplit=2)
            if len(component_pieces) != 2:
                raise ValueError(
                    f"Invalid actor id component `{component}` in "
                    f"`{candidate}`: must contain either an encoded state type "
                    "or state type string, separated from a key by a `:`."
                )
            # NB: We do not use `from_key` in this case, because the key
            # component is assumed to already be encoded.
            state_type_tag = _state_type_tag(
                StateTypeName(component_pieces[0])
            )
            actor_key = component_pieces[1]
            result.append(ActorId(f"{state_type_tag}:{actor_key}"))
        if len(result) == 0:
            raise ValueError("Cannot create empty ActorId.")
        return ActorId('/'.join(result))

    @classmethod
    def from_key(
        cls, state_type: StateTypeName, actor_key: ActorKey
    ) -> ActorId:
        validate_ascii(
            actor_key,
            'actor_key',
            MAX_ACTOR_ID_LENGTH,
            illegal_characters="\0\n\\",
            error_type=InvalidActorIdError,
        )
        return ActorId(
            f"{_state_type_tag(state_type)}:{_actor_key_encode(actor_key)}"
        )

    @property
    def key(self) -> ActorKey:
        # If we don't find a slash, then the key isn't compound and this
        # will return -1. Regardless: we'll add one below to either skip the
        # slash, or to start from the 0-th position.
        last_key_start_idx = self.rfind('/')
        return _actor_key_decode(
            self[last_key_start_idx + 1 + _STATE_TYPE_TAG_LENGTH + 1:]
        )

    def colocate(
        self,
        colocated_state_type: StateTypeName,
        colocated_actor_key: ActorKey,
    ) -> ActorId:
        colocated_id = ActorId.from_key(
            colocated_state_type,
            colocated_actor_key,
        )
        return ActorId(f"{self}/{colocated_id}")


# A cache of state type tags that have already been computed.
_state_type_tags: dict[StateTypeName, str] = {}
# The length of a state type tag: a sha1 hash, base64 encoded, with the
# trailing `=` stripped.
_STATE_TYPE_TAG_LENGTH = 14


def _state_type_tag(state_type: StateTypeName) -> str:
    state_type_tag = _state_type_tags.get(state_type)
    if state_type_tag is None:
        state_type_bytes = bytearray(
            hashlib.sha1(state_type.encode()).digest()
        )
        state_type_bytes = state_type_bytes[0:len(state_type_bytes) // 2]
        # NOTE: The high order byte is always zeroed to allow for forwards
        # compatibly using a more compact type tag format in the future.
        state_type_bytes[0] = 0
        state_type_tag = base64.urlsafe_b64encode(state_type_bytes).decode()
        # NOTE: base64 uses trailing equal signs as padding when an input's
        # length isn't a multiple of three: since our input length is fixed,
        # we can expect to find padding.
        assert state_type_tag[-1] == '=' and state_type_tag[-2] == '='
        state_type_tag = state_type_tag[:-2]
        assert len(state_type_tag) == _STATE_TYPE_TAG_LENGTH
        _state_type_tags[state_type] = state_type_tag
    return state_type_tag


def _actor_key_encode(actor_key: ActorKey) -> str:
    return actor_key.replace("/", "\\")


def _actor_key_decode(actor_key_encoded: str) -> ActorKey:
    return actor_key_encoded.replace("\\", "/")


def service_to_state_type(service: ServiceName) -> StateTypeName:
    """Converts a `ServiceName` into a `StateTypeName`.

    We currently support a single interface/service per state type, with a
    hardcoded name.
    """
    assert service.endswith("Interface"), f"Invalid service name: {service}"
    return StateTypeName(service[:-9])


def state_type_to_service(state_type: StateTypeName) -> ServiceName:
    """Converts a `StateTypeName` into a `ServiceName`.

    See `service_to_state_type`.
    """
    assert not state_type.endswith(
        "Interface"
    ), f"Invalid state type name: {state_type}"
    return ServiceName(f"{state_type}Interface")


def assert_type(
    t: Any,
    types: list[type[Any]],
    *,
    may_be_subclass: bool = True,
) -> None:
    """Check that 't' is an instance of one of the expected types.

    Raises TypeError if 't' is not one of the expected types.
    """

    def check(t: Any, expected_type: Any) -> bool:
        if may_be_subclass:
            return isinstance(t, expected_type)
        else:
            return type(t) is expected_type

    if any([check(t, expected_type) for expected_type in types]):
        return

    def type_name(cls):
        return f'{cls.__module__}.{cls.__qualname__}'

    if may_be_subclass:
        raise TypeError(
            f'{type_name(type(t))} is not an instance or subclass of one of the expected '
            f'type(s): {[type_name(expected_type) for expected_type in types]}'
        )
    else:
        raise TypeError(
            f'{type_name(type(t))} is not a non-subclass instance of one of the expected '
            f'type(s): {[type_name(expected_type) for expected_type in types]}'
        )


def validate_ascii(
    value: Optional[str],
    field_name: str,
    length_limit: int,
    *,
    illegal_characters: str = "",
    error_type: type[ValueError] = ValueError,
) -> None:
    if value is None:
        return
    if not isinstance(value, str):
        raise TypeError(
            f"The '{field_name}' option must be of type 'str', but got "
            f"'{type(value).__name__}'"
        )
    if len(value) > length_limit:
        raise error_type(
            f"The '{field_name}' option must be at most "
            f"{length_limit} characters long; the given value "
            f"is {len(value)} characters long"
        )
    if not value.isascii():
        raise error_type(
            f"The '{field_name}' option must be an ASCII string; the "
            f"given value '{value}' is not ASCII"
        )
    found = [c for c in value if c in illegal_characters]
    if len(found) > 0:
        raise error_type(
            f"The '{field_name}' option contained illegal characters: "
            f"{found!r}. The value was: {value!r}."
        )


class InvalidActorIdError(ValueError):
    pass


class InvalidIdempotencyKeyError(ValueError):
    pass


class InvalidBearerTokenError(ValueError):
    pass
