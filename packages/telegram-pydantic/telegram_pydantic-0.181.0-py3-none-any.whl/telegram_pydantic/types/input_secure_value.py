from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputSecureValue(BaseModel):
    """
    types.InputSecureValue
    ID: 0xdb21d0a7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputSecureValue'] = pydantic.Field(
        'types.InputSecureValue',
        alias='_'
    )

    type: "base.SecureValueType"
    data: typing.Optional["base.SecureData"] = None
    front_side: typing.Optional["base.InputSecureFile"] = None
    reverse_side: typing.Optional["base.InputSecureFile"] = None
    selfie: typing.Optional["base.InputSecureFile"] = None
    translation: typing.Optional[list["base.InputSecureFile"]] = None
    files: typing.Optional[list["base.InputSecureFile"]] = None
    plain_data: typing.Optional["base.SecurePlainData"] = None
