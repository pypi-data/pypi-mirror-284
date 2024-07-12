from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetEmojiStickers(BaseModel):
    """
    functions.channels.SetEmojiStickers
    ID: 0x3cd930b7
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.SetEmojiStickers'] = pydantic.Field(
        'functions.channels.SetEmojiStickers',
        alias='_'
    )

    channel: "base.InputChannel"
    stickerset: "base.InputStickerSet"
