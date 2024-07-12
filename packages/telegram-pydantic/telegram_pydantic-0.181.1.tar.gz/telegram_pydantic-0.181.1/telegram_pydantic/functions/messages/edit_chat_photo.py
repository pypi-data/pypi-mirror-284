from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditChatPhoto(BaseModel):
    """
    functions.messages.EditChatPhoto
    ID: 0x35ddd674
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditChatPhoto'] = pydantic.Field(
        'functions.messages.EditChatPhoto',
        alias='_'
    )

    chat_id: int
    photo: "base.InputChatPhoto"
