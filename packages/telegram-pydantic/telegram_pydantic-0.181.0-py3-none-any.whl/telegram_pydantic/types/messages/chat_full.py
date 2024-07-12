from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatFull(BaseModel):
    """
    types.messages.ChatFull
    ID: 0xe5d7d19c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ChatFull'] = pydantic.Field(
        'types.messages.ChatFull',
        alias='_'
    )

    full_chat: "base.ChatFull"
    chats: list["base.Chat"]
    users: list["base.User"]
