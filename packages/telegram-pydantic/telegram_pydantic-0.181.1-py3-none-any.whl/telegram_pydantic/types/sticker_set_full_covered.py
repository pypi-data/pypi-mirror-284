from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetFullCovered(BaseModel):
    """
    types.StickerSetFullCovered
    ID: 0x40d13c0e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerSetFullCovered'] = pydantic.Field(
        'types.StickerSetFullCovered',
        alias='_'
    )

    set: "base.StickerSet"
    packs: list["base.StickerPack"]
    keywords: list["base.StickerKeyword"]
    documents: list["base.Document"]
