from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorFiles(BaseModel):
    """
    types.SecureValueErrorFiles
    ID: 0x666220e9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorFiles'] = pydantic.Field(
        'types.SecureValueErrorFiles',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: list[bytes]
    text: str
