from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecurePlainPhone(BaseModel):
    """
    types.SecurePlainPhone
    ID: 0x7d6099dd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecurePlainPhone'] = pydantic.Field(
        'types.SecurePlainPhone',
        alias='_'
    )

    phone: str
