from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiGroupGreeting(BaseModel):
    """
    types.EmojiGroupGreeting
    ID: 0x80d26cc7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiGroupGreeting'] = pydantic.Field(
        'types.EmojiGroupGreeting',
        alias='_'
    )

    title: str
    icon_emoji_id: int
    emoticons: list[str]
