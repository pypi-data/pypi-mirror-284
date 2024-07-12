from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiURL(BaseModel):
    """
    functions.messages.GetEmojiURL
    ID: 0xd5b10c26
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiURL'] = pydantic.Field(
        'functions.messages.GetEmojiURL',
        alias='_'
    )

    lang_code: str
