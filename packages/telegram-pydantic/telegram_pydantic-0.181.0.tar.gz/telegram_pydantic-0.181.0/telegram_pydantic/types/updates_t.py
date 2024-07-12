from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Updates(BaseModel):
    """
    types.Updates
    ID: 0x74ae4240
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Updates'] = pydantic.Field(
        'types.Updates',
        alias='_'
    )

    updates: list["base.Update"]
    users: list["base.User"]
    chats: list["base.Chat"]
    date: int
    seq: int
