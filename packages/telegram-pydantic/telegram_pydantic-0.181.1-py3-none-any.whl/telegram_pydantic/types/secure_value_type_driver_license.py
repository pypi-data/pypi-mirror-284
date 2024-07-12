from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeDriverLicense(BaseModel):
    """
    types.SecureValueTypeDriverLicense
    ID: 0x6e425c4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeDriverLicense'] = pydantic.Field(
        'types.SecureValueTypeDriverLicense',
        alias='_'
    )

