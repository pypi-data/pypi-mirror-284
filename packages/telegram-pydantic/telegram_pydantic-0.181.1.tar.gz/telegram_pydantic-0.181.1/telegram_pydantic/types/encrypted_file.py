from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedFile(BaseModel):
    """
    types.EncryptedFile
    ID: 0xa8008cd8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedFile'] = pydantic.Field(
        'types.EncryptedFile',
        alias='_'
    )

    id: int
    access_hash: int
    size: int
    dc_id: int
    key_fingerprint: int
