from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorFrontSide(BaseModel):
    """
    types.SecureValueErrorFrontSide
    ID: 0xbe3dfa
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorFrontSide'] = pydantic.Field(
        'types.SecureValueErrorFrontSide',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: bytes
    text: str
