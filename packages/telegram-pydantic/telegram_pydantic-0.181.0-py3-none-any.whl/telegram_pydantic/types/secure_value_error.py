from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueError(BaseModel):
    """
    types.SecureValueError
    ID: 0x869d758f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueError'] = pydantic.Field(
        'types.SecureValueError',
        alias='_'
    )

    type: "base.SecureValueType"
    hash: bytes
    text: str
