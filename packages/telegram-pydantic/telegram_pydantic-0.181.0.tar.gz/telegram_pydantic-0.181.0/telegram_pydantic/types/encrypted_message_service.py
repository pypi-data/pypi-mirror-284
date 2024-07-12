from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedMessageService(BaseModel):
    """
    types.EncryptedMessageService
    ID: 0x23734b06
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedMessageService'] = pydantic.Field(
        'types.EncryptedMessageService',
        alias='_'
    )

    random_id: int
    chat_id: int
    date: int
    bytes: bytes
