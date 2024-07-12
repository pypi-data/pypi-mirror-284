from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureCredentialsEncrypted(BaseModel):
    """
    types.SecureCredentialsEncrypted
    ID: 0x33f0ea47
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureCredentialsEncrypted'] = pydantic.Field(
        'types.SecureCredentialsEncrypted',
        alias='_'
    )

    data: bytes
    hash: bytes
    secret: bytes
