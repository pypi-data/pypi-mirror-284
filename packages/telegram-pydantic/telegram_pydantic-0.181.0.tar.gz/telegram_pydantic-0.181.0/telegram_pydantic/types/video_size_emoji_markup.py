from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class VideoSizeEmojiMarkup(BaseModel):
    """
    types.VideoSizeEmojiMarkup
    ID: 0xf85c413c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.VideoSizeEmojiMarkup'] = pydantic.Field(
        'types.VideoSizeEmojiMarkup',
        alias='_'
    )

    emoji_id: int
    background_colors: list[int]
