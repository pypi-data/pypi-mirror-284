from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetCovered(BaseModel):
    """
    types.StickerSetCovered
    ID: 0x6410a5d2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerSetCovered'] = pydantic.Field(
        'types.StickerSetCovered',
        alias='_'
    )

    set: "base.StickerSet"
    cover: "base.Document"
