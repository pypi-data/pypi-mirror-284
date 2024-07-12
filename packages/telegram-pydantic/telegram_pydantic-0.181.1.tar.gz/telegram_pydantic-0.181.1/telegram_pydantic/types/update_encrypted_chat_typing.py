from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateEncryptedChatTyping(BaseModel):
    """
    types.UpdateEncryptedChatTyping
    ID: 0x1710f156
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateEncryptedChatTyping'] = pydantic.Field(
        'types.UpdateEncryptedChatTyping',
        alias='_'
    )

    chat_id: int
