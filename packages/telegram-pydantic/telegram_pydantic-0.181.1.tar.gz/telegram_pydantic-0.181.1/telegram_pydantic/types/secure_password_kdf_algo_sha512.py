from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecurePasswordKdfAlgoSHA512(BaseModel):
    """
    types.SecurePasswordKdfAlgoSHA512
    ID: 0x86471d92
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecurePasswordKdfAlgoSHA512'] = pydantic.Field(
        'types.SecurePasswordKdfAlgoSHA512',
        alias='_'
    )

    salt: bytes
