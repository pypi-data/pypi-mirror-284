from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorData(BaseModel):
    """
    types.SecureValueErrorData
    ID: 0xe8a40bd9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorData'] = pydantic.Field(
        'types.SecureValueErrorData',
        alias='_'
    )

    type: "base.SecureValueType"
    data_hash: bytes
    field: str
    text: str
