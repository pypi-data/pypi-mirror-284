from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserStatusOffline(BaseModel):
    """
    types.UserStatusOffline
    ID: 0x8c703f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserStatusOffline'] = pydantic.Field(
        'types.UserStatusOffline',
        alias='_'
    )

    was_online: int
