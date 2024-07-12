from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPageAttributeStickerSet(BaseModel):
    """
    types.WebPageAttributeStickerSet
    ID: 0x50cc03d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPageAttributeStickerSet'] = pydantic.Field(
        'types.WebPageAttributeStickerSet',
        alias='_'
    )

    stickers: list["base.Document"]
    emojis: typing.Optional[bool] = None
    text_color: typing.Optional[bool] = None
