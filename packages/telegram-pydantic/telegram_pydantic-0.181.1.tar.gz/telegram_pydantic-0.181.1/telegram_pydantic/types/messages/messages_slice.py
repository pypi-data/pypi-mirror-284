from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessagesSlice(BaseModel):
    """
    types.messages.MessagesSlice
    ID: 0x3a54685e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.MessagesSlice'] = pydantic.Field(
        'types.messages.MessagesSlice',
        alias='_'
    )

    count: int
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
    inexact: typing.Optional[bool] = None
    next_rate: typing.Optional[int] = None
    offset_id_offset: typing.Optional[int] = None
