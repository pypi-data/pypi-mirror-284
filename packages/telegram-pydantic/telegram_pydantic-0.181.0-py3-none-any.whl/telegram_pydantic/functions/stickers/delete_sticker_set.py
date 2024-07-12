from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteStickerSet(BaseModel):
    """
    functions.stickers.DeleteStickerSet
    ID: 0x87704394
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.DeleteStickerSet'] = pydantic.Field(
        'functions.stickers.DeleteStickerSet',
        alias='_'
    )

    stickerset: "base.InputStickerSet"
