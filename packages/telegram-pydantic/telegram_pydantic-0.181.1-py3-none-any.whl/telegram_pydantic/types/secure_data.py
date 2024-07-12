from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureData(BaseModel):
    """
    types.SecureData
    ID: 0x8aeabec3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureData'] = pydantic.Field(
        'types.SecureData',
        alias='_'
    )

    data: bytes
    data_hash: bytes
    secret: bytes
