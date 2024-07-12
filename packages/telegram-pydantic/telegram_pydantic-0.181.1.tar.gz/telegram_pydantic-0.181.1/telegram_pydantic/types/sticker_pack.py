from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerPack(BaseModel):
    """
    types.StickerPack
    ID: 0x12b299d4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerPack'] = pydantic.Field(
        'types.StickerPack',
        alias='_'
    )

    emoticon: str
    documents: list[int]
