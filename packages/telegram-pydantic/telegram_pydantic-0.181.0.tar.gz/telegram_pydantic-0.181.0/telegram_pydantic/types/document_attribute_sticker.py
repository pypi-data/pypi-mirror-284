from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeSticker(BaseModel):
    """
    types.DocumentAttributeSticker
    ID: 0x6319d612
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeSticker'] = pydantic.Field(
        'types.DocumentAttributeSticker',
        alias='_'
    )

    alt: str
    stickerset: "base.InputStickerSet"
    mask: typing.Optional[bool] = None
    mask_coords: typing.Optional["base.MaskCoords"] = None
