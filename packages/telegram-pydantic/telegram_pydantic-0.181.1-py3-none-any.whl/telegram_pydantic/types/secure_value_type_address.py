from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeAddress(BaseModel):
    """
    types.SecureValueTypeAddress
    ID: 0xcbe31e26
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeAddress'] = pydantic.Field(
        'types.SecureValueTypeAddress',
        alias='_'
    )

