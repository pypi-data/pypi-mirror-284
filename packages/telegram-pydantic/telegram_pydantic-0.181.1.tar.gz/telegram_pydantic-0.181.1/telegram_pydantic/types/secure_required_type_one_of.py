from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureRequiredTypeOneOf(BaseModel):
    """
    types.SecureRequiredTypeOneOf
    ID: 0x27477b4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureRequiredTypeOneOf'] = pydantic.Field(
        'types.SecureRequiredTypeOneOf',
        alias='_'
    )

    types: list["base.SecureRequiredType"]
