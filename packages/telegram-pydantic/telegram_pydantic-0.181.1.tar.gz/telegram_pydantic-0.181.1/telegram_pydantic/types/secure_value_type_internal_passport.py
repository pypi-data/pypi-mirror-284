from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeInternalPassport(BaseModel):
    """
    types.SecureValueTypeInternalPassport
    ID: 0x99a48f23
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeInternalPassport'] = pydantic.Field(
        'types.SecureValueTypeInternalPassport',
        alias='_'
    )

