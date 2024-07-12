from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValue(BaseModel):
    """
    types.SecureValue
    ID: 0x187fa0ca
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValue'] = pydantic.Field(
        'types.SecureValue',
        alias='_'
    )

    type: "base.SecureValueType"
    hash: bytes
    data: typing.Optional["base.SecureData"] = None
    front_side: typing.Optional["base.SecureFile"] = None
    reverse_side: typing.Optional["base.SecureFile"] = None
    selfie: typing.Optional["base.SecureFile"] = None
    translation: typing.Optional[list["base.SecureFile"]] = None
    files: typing.Optional[list["base.SecureFile"]] = None
    plain_data: typing.Optional["base.SecurePlainData"] = None
