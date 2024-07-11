from datetime import datetime

import strawberry

from strawberry_django_jwt.object_types import TokenPayloadType


@strawberry.type(name="JWTRefreshedPayload")
class RefreshedTokenType:
    payload: TokenPayloadType
    token: str
    refresh_token: str
    refresh_expires_in: int


@strawberry.type(name="JWTRevokedPayload")
class RevokeType:
    revoked: datetime
