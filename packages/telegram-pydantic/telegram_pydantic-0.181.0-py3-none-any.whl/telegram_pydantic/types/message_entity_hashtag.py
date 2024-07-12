from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityHashtag(BaseModel):
    """
    types.MessageEntityHashtag
    ID: 0x6f635b0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityHashtag'] = pydantic.Field(
        'types.MessageEntityHashtag',
        alias='_'
    )

    offset: int
    length: int
