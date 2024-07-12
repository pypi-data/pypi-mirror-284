from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFullChat(BaseModel):
    """
    functions.messages.GetFullChat
    ID: 0xaeb00b34
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetFullChat'] = pydantic.Field(
        'functions.messages.GetFullChat',
        alias='_'
    )

    chat_id: int
