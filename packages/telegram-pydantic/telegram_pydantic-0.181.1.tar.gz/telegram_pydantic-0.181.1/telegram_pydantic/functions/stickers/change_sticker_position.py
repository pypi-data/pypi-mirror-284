from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChangeStickerPosition(BaseModel):
    """
    functions.stickers.ChangeStickerPosition
    ID: 0xffb6d4ca
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.ChangeStickerPosition'] = pydantic.Field(
        'functions.stickers.ChangeStickerPosition',
        alias='_'
    )

    sticker: "base.InputDocument"
    position: int
