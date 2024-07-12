from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeUtilityBill(BaseModel):
    """
    types.SecureValueTypeUtilityBill
    ID: 0xfc36954e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeUtilityBill'] = pydantic.Field(
        'types.SecureValueTypeUtilityBill',
        alias='_'
    )

