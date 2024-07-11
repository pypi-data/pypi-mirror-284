from dataclasses import dataclass
from resemble.aio.types import GrpcMetadata
from resemble.aio.types import InvalidActorIdError as InvalidActorIdError
from resemble.aio.types import (
    InvalidBearerTokenError,
    InvalidIdempotencyKeyError,
    validate_ascii,
)
from resemble.settings import (
    MAX_BEARER_TOKEN_LENGTH,
    MAX_IDEMPOTENCY_KEY_LENGTH,
)
from typing import Optional


@dataclass(kw_only=True, frozen=True)
class Options:
    """Options for RPCs."""
    idempotency_key: Optional[str] = None
    idempotency_alias: Optional[str] = None
    generate_idempotency: bool = False
    metadata: Optional[GrpcMetadata] = None
    bearer_token: Optional[str] = None

    def __post_init__(self):
        validate_ascii(
            self.idempotency_key,
            'idempotency_key',
            MAX_IDEMPOTENCY_KEY_LENGTH,
            error_type=InvalidIdempotencyKeyError,
            illegal_characters='\n',
        )
        validate_ascii(
            self.bearer_token,
            'bearer_token',
            MAX_BEARER_TOKEN_LENGTH,
            error_type=InvalidBearerTokenError,
            illegal_characters='\n',
        )

        if (
            self.idempotency_key is not None and
            self.idempotency_alias is not None
        ):
            raise TypeError(
                "options: only one of 'idempotency_key' or 'idempotency_alias' "
                "should be set"
            )


class MixedContextsError(ValueError):
    pass
