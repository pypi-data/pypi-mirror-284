from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedChatEmpty(BaseModel):
    """
    types.EncryptedChatEmpty
    ID: 0xab7ec0a0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedChatEmpty'] = pydantic.Field(
        'types.EncryptedChatEmpty',
        alias='_'
    )

    id: int
