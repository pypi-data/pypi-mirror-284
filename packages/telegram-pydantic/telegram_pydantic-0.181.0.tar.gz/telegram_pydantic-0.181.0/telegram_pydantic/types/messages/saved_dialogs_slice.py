from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedDialogsSlice(BaseModel):
    """
    types.messages.SavedDialogsSlice
    ID: 0x44ba9dd9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedDialogsSlice'] = pydantic.Field(
        'types.messages.SavedDialogsSlice',
        alias='_'
    )

    count: int
    dialogs: list["base.SavedDialog"]
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
