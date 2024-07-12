from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedChatWaiting(BaseModel):
    """
    types.EncryptedChatWaiting
    ID: 0x66b25953
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedChatWaiting'] = pydantic.Field(
        'types.EncryptedChatWaiting',
        alias='_'
    )

    id: int
    access_hash: int
    date: int
    admin_id: int
    participant_id: int
