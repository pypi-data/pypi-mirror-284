from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedChatRequested(BaseModel):
    """
    types.EncryptedChatRequested
    ID: 0x48f1d94c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedChatRequested'] = pydantic.Field(
        'types.EncryptedChatRequested',
        alias='_'
    )

    id: int
    access_hash: int
    date: int
    admin_id: int
    participant_id: int
    g_a: bytes
    folder_id: typing.Optional[int] = None
