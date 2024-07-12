from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class VideoSizeStickerMarkup(BaseModel):
    """
    types.VideoSizeStickerMarkup
    ID: 0xda082fe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.VideoSizeStickerMarkup'] = pydantic.Field(
        'types.VideoSizeStickerMarkup',
        alias='_'
    )

    stickerset: "base.InputStickerSet"
    sticker_id: int
    background_colors: list[int]
