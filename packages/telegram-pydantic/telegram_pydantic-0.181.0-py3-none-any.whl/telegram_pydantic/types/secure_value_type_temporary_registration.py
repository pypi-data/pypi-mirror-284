from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeTemporaryRegistration(BaseModel):
    """
    types.SecureValueTypeTemporaryRegistration
    ID: 0xea02ec33
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeTemporaryRegistration'] = pydantic.Field(
        'types.SecureValueTypeTemporaryRegistration',
        alias='_'
    )

