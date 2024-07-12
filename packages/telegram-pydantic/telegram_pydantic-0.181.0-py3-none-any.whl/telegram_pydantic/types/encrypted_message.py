from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedMessage(BaseModel):
    """
    types.EncryptedMessage
    ID: 0xed18c118
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedMessage'] = pydantic.Field(
        'types.EncryptedMessage',
        alias='_'
    )

    random_id: int
    chat_id: int
    date: int
    bytes: bytes
    file: "base.EncryptedFile"
