from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorSelfie(BaseModel):
    """
    types.SecureValueErrorSelfie
    ID: 0xe537ced6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorSelfie'] = pydantic.Field(
        'types.SecureValueErrorSelfie',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: bytes
    text: str
