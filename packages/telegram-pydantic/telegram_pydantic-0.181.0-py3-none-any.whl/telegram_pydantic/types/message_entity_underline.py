from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityUnderline(BaseModel):
    """
    types.MessageEntityUnderline
    ID: 0x9c4e7e8b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityUnderline'] = pydantic.Field(
        'types.MessageEntityUnderline',
        alias='_'
    )

    offset: int
    length: int
