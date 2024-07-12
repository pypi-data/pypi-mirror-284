from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityPhone(BaseModel):
    """
    types.MessageEntityPhone
    ID: 0x9b69e34b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityPhone'] = pydantic.Field(
        'types.MessageEntityPhone',
        alias='_'
    )

    offset: int
    length: int
