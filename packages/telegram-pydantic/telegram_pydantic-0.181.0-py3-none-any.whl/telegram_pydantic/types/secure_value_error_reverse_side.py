from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorReverseSide(BaseModel):
    """
    types.SecureValueErrorReverseSide
    ID: 0x868a2aa5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorReverseSide'] = pydantic.Field(
        'types.SecureValueErrorReverseSide',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: bytes
    text: str
