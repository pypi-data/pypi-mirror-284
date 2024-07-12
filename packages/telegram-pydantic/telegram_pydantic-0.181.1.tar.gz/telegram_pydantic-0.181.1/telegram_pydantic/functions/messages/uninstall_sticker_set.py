from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UninstallStickerSet(BaseModel):
    """
    functions.messages.UninstallStickerSet
    ID: 0xf96e55de
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UninstallStickerSet'] = pydantic.Field(
        'functions.messages.UninstallStickerSet',
        alias='_'
    )

    stickerset: "base.InputStickerSet"
