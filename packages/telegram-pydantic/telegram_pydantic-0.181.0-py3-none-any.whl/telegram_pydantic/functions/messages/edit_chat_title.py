from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditChatTitle(BaseModel):
    """
    functions.messages.EditChatTitle
    ID: 0x73783ffd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditChatTitle'] = pydantic.Field(
        'functions.messages.EditChatTitle',
        alias='_'
    )

    chat_id: int
    title: str
