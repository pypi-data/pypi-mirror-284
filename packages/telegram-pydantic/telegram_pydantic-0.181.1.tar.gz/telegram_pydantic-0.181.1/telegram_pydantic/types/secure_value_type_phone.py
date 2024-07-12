from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypePhone(BaseModel):
    """
    types.SecureValueTypePhone
    ID: 0xb320aadb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypePhone'] = pydantic.Field(
        'types.SecureValueTypePhone',
        alias='_'
    )

