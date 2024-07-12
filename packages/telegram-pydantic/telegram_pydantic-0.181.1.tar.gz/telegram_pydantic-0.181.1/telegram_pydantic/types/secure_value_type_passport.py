from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypePassport(BaseModel):
    """
    types.SecureValueTypePassport
    ID: 0x3dac6a00
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypePassport'] = pydantic.Field(
        'types.SecureValueTypePassport',
        alias='_'
    )

