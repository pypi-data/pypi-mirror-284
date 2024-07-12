from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureFile(BaseModel):
    """
    types.SecureFile
    ID: 0x7d09c27e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureFile'] = pydantic.Field(
        'types.SecureFile',
        alias='_'
    )

    id: int
    access_hash: int
    size: int
    dc_id: int
    date: int
    file_hash: bytes
    secret: bytes
