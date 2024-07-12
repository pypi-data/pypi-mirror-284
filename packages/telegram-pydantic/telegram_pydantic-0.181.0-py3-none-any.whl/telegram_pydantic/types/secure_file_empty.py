from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureFileEmpty(BaseModel):
    """
    types.SecureFileEmpty
    ID: 0x64199744
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureFileEmpty'] = pydantic.Field(
        'types.SecureFileEmpty',
        alias='_'
    )

