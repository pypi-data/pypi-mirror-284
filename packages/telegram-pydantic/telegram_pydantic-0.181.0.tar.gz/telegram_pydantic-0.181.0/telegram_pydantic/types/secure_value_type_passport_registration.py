from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypePassportRegistration(BaseModel):
    """
    types.SecureValueTypePassportRegistration
    ID: 0x99e3806a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypePassportRegistration'] = pydantic.Field(
        'types.SecureValueTypePassportRegistration',
        alias='_'
    )

