from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReplaceSticker(BaseModel):
    """
    functions.stickers.ReplaceSticker
    ID: 0x4696459a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.ReplaceSticker'] = pydantic.Field(
        'functions.stickers.ReplaceSticker',
        alias='_'
    )

    sticker: "base.InputDocument"
    new_sticker: "base.InputStickerSetItem"
