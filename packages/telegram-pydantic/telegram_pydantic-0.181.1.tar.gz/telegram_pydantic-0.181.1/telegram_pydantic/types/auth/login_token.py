from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LoginToken(BaseModel):
    """
    types.auth.LoginToken
    ID: 0x629f1980
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.LoginToken'] = pydantic.Field(
        'types.auth.LoginToken',
        alias='_'
    )

    expires: int
    token: bytes
