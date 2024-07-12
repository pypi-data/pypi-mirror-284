from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntitySpoiler(BaseModel):
    """
    types.MessageEntitySpoiler
    ID: 0x32ca960f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntitySpoiler'] = pydantic.Field(
        'types.MessageEntitySpoiler',
        alias='_'
    )

    offset: int
    length: int
