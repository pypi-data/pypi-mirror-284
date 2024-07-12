from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityItalic(BaseModel):
    """
    types.MessageEntityItalic
    ID: 0x826f8b60
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityItalic'] = pydantic.Field(
        'types.MessageEntityItalic',
        alias='_'
    )

    offset: int
    length: int
