from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChangeSticker(BaseModel):
    """
    functions.stickers.ChangeSticker
    ID: 0xf5537ebc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.ChangeSticker'] = pydantic.Field(
        'functions.stickers.ChangeSticker',
        alias='_'
    )

    sticker: "base.InputDocument"
    emoji: typing.Optional[str] = None
    mask_coords: typing.Optional["base.MaskCoords"] = None
    keywords: typing.Optional[str] = None
