from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityUnknown(BaseModel):
    """
    types.MessageEntityUnknown
    ID: 0xbb92ba95
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityUnknown'] = pydantic.Field(
        'types.MessageEntityUnknown',
        alias='_'
    )

    offset: int
    length: int
