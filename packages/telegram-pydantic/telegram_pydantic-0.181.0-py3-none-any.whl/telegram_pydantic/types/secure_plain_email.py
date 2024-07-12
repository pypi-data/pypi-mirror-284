from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecurePlainEmail(BaseModel):
    """
    types.SecurePlainEmail
    ID: 0x21ec5a5f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecurePlainEmail'] = pydantic.Field(
        'types.SecurePlainEmail',
        alias='_'
    )

    email: str
