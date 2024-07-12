from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FavedStickers(BaseModel):
    """
    types.messages.FavedStickers
    ID: 0x2cb51097
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.FavedStickers'] = pydantic.Field(
        'types.messages.FavedStickers',
        alias='_'
    )

    hash: int
    packs: list["base.StickerPack"]
    stickers: list["base.Document"]
