from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Authorization(BaseModel):
    """
    types.auth.Authorization
    ID: 0x2ea2c0d4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.Authorization'] = pydantic.Field(
        'types.auth.Authorization',
        alias='_'
    )

    user: "base.User"
    setup_password_required: typing.Optional[bool] = None
    otherwise_relogin_days: typing.Optional[int] = None
    tmp_sessions: typing.Optional[int] = None
    future_auth_token: typing.Optional[bytes] = None
