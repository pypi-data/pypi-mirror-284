from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentStickers(BaseModel):
    """
    types.messages.RecentStickers
    ID: 0x88d37c56
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.RecentStickers'] = pydantic.Field(
        'types.messages.RecentStickers',
        alias='_'
    )

    hash: int
    packs: list["base.StickerPack"]
    stickers: list["base.Document"]
    dates: list[int]
