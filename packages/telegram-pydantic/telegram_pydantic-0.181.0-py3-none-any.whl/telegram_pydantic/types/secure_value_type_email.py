from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeEmail(BaseModel):
    """
    types.SecureValueTypeEmail
    ID: 0x8e3ca7ee
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeEmail'] = pydantic.Field(
        'types.SecureValueTypeEmail',
        alias='_'
    )

