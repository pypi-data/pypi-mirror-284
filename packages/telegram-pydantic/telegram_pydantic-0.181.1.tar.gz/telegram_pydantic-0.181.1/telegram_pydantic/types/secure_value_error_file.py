from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorFile(BaseModel):
    """
    types.SecureValueErrorFile
    ID: 0x7a700873
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorFile'] = pydantic.Field(
        'types.SecureValueErrorFile',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: bytes
    text: str
