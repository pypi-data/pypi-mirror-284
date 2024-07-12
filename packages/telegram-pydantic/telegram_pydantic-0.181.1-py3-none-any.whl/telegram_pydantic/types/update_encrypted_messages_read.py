from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateEncryptedMessagesRead(BaseModel):
    """
    types.UpdateEncryptedMessagesRead
    ID: 0x38fe25b7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateEncryptedMessagesRead'] = pydantic.Field(
        'types.UpdateEncryptedMessagesRead',
        alias='_'
    )

    chat_id: int
    max_date: int
    date: int
