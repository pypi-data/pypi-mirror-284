from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStickerSet(BaseModel):
    """
    functions.messages.GetStickerSet
    ID: 0xc8a0ec74
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetStickerSet'] = pydantic.Field(
        'functions.messages.GetStickerSet',
        alias='_'
    )

    stickerset: "base.InputStickerSet"
    hash: int
