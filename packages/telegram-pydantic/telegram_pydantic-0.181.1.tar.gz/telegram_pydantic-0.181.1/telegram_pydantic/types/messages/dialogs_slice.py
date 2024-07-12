from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogsSlice(BaseModel):
    """
    types.messages.DialogsSlice
    ID: 0x71e094f3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.DialogsSlice'] = pydantic.Field(
        'types.messages.DialogsSlice',
        alias='_'
    )

    count: int
    dialogs: list["base.Dialog"]
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
