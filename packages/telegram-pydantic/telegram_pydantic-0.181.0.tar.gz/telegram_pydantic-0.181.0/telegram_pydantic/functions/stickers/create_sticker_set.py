from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CreateStickerSet(BaseModel):
    """
    functions.stickers.CreateStickerSet
    ID: 0x9021ab67
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.CreateStickerSet'] = pydantic.Field(
        'functions.stickers.CreateStickerSet',
        alias='_'
    )

    user_id: "base.InputUser"
    title: str
    short_name: str
    stickers: list["base.InputStickerSetItem"]
    masks: typing.Optional[bool] = None
    emojis: typing.Optional[bool] = None
    text_color: typing.Optional[bool] = None
    thumb: typing.Optional["base.InputDocument"] = None
    software: typing.Optional[str] = None
