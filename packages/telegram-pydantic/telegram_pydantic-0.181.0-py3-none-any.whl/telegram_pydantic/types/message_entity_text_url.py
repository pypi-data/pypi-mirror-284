from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityTextUrl(BaseModel):
    """
    types.MessageEntityTextUrl
    ID: 0x76a6d327
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityTextUrl'] = pydantic.Field(
        'types.MessageEntityTextUrl',
        alias='_'
    )

    offset: int
    length: int
    url: str
