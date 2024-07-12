from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeBankStatement(BaseModel):
    """
    types.SecureValueTypeBankStatement
    ID: 0x89137c0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeBankStatement'] = pydantic.Field(
        'types.SecureValueTypeBankStatement',
        alias='_'
    )

