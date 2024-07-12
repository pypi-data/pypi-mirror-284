from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatsSlice(BaseModel):
    """
    types.messages.ChatsSlice
    ID: 0x9cd81144
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ChatsSlice'] = pydantic.Field(
        'types.messages.ChatsSlice',
        alias='_'
    )

    count: int
    chats: list["base.Chat"]
