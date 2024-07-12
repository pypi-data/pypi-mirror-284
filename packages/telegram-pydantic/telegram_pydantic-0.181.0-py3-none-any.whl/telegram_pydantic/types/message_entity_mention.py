from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityMention(BaseModel):
    """
    types.MessageEntityMention
    ID: 0xfa04579d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityMention'] = pydantic.Field(
        'types.MessageEntityMention',
        alias='_'
    )

    offset: int
    length: int
