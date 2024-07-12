from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStickers(BaseModel):
    """
    functions.messages.GetStickers
    ID: 0xd5a5d3a1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetStickers'] = pydantic.Field(
        'functions.messages.GetStickers',
        alias='_'
    )

    emoticon: str
    hash: int
