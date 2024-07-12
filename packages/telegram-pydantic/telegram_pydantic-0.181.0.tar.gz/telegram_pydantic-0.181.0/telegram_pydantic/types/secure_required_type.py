from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureRequiredType(BaseModel):
    """
    types.SecureRequiredType
    ID: 0x829d99da
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureRequiredType'] = pydantic.Field(
        'types.SecureRequiredType',
        alias='_'
    )

    type: "base.SecureValueType"
    native_names: typing.Optional[bool] = None
    selfie_required: typing.Optional[bool] = None
    translation_required: typing.Optional[bool] = None
