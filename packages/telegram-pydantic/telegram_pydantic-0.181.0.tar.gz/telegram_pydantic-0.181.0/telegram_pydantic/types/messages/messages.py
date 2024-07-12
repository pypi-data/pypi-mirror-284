from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Messages(BaseModel):
    """
    types.messages.Messages
    ID: 0x8c718e87
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.Messages'] = pydantic.Field(
        'types.messages.Messages',
        alias='_'
    )

    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
