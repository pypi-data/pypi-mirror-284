from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditChatAdmin(BaseModel):
    """
    functions.messages.EditChatAdmin
    ID: 0xa85bd1c2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditChatAdmin'] = pydantic.Field(
        'functions.messages.EditChatAdmin',
        alias='_'
    )

    chat_id: int
    user_id: "base.InputUser"
    is_admin: bool
