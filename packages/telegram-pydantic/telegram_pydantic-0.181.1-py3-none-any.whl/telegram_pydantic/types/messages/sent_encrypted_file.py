from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentEncryptedFile(BaseModel):
    """
    types.messages.SentEncryptedFile
    ID: 0x9493ff32
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SentEncryptedFile'] = pydantic.Field(
        'types.messages.SentEncryptedFile',
        alias='_'
    )

    date: int
    file: "base.EncryptedFile"
