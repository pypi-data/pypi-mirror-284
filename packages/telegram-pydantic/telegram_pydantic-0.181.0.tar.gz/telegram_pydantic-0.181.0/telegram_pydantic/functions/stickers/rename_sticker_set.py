from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RenameStickerSet(BaseModel):
    """
    functions.stickers.RenameStickerSet
    ID: 0x124b1c00
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.RenameStickerSet'] = pydantic.Field(
        'functions.stickers.RenameStickerSet',
        alias='_'
    )

    stickerset: "base.InputStickerSet"
    title: str
