from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LoggedOut(BaseModel):
    """
    types.auth.LoggedOut
    ID: 0xc3a2835f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.LoggedOut'] = pydantic.Field(
        'types.auth.LoggedOut',
        alias='_'
    )

    future_auth_token: typing.Optional[bytes] = None
