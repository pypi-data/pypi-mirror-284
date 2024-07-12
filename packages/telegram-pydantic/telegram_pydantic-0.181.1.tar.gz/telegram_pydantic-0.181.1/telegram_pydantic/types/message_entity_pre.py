from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityPre(BaseModel):
    """
    types.MessageEntityPre
    ID: 0x73924be0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityPre'] = pydantic.Field(
        'types.MessageEntityPre',
        alias='_'
    )

    offset: int
    length: int
    language: str
