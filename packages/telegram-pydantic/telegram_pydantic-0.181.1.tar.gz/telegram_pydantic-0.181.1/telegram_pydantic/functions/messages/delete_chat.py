from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteChat(BaseModel):
    """
    functions.messages.DeleteChat
    ID: 0x5bd0ee50
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteChat'] = pydantic.Field(
        'functions.messages.DeleteChat',
        alias='_'
    )

    chat_id: int
