from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetMultiCovered(BaseModel):
    """
    types.StickerSetMultiCovered
    ID: 0x3407e51b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerSetMultiCovered'] = pydantic.Field(
        'types.StickerSetMultiCovered',
        alias='_'
    )

    set: "base.StickerSet"
    covers: list["base.Document"]
