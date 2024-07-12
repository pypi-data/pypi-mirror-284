from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedChat(BaseModel):
    """
    types.EncryptedChat
    ID: 0x61f0d4c7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedChat'] = pydantic.Field(
        'types.EncryptedChat',
        alias='_'
    )

    id: int
    access_hash: int
    date: int
    admin_id: int
    participant_id: int
    g_a_or_b: bytes
    key_fingerprint: int
