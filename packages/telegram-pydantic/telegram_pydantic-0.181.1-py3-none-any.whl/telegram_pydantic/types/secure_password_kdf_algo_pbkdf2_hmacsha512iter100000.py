from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000(BaseModel):
    """
    types.SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000
    ID: 0xbbf2dda0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000'] = pydantic.Field(
        'types.SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000',
        alias='_'
    )

    salt: bytes
