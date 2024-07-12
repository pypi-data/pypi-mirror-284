from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetStickers(BaseModel):
    """
    functions.channels.SetStickers
    ID: 0xea8ca4f9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.SetStickers'] = pydantic.Field(
        'functions.channels.SetStickers',
        alias='_'
    )

    channel: "base.InputChannel"
    stickerset: "base.InputStickerSet"
