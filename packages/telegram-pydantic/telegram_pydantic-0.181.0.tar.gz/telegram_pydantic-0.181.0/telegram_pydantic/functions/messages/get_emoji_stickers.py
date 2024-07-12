from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiStickers(BaseModel):
    """
    functions.messages.GetEmojiStickers
    ID: 0xfbfca18f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiStickers'] = pydantic.Field(
        'functions.messages.GetEmojiStickers',
        alias='_'
    )

    hash: int
