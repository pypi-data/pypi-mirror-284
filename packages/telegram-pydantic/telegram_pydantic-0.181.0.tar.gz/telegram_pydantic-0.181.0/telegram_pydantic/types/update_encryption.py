from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateEncryption(BaseModel):
    """
    types.UpdateEncryption
    ID: 0xb4a2e88d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateEncryption'] = pydantic.Field(
        'types.UpdateEncryption',
        alias='_'
    )

    chat: "base.EncryptedChat"
    date: int
