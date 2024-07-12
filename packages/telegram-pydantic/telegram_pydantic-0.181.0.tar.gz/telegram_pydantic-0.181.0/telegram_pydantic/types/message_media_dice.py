from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaDice(BaseModel):
    """
    types.MessageMediaDice
    ID: 0x3f7ee58b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaDice'] = pydantic.Field(
        'types.MessageMediaDice',
        alias='_'
    )

    value: int
    emoticon: str
