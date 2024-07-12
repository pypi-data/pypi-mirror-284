from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetNoCovered(BaseModel):
    """
    types.StickerSetNoCovered
    ID: 0x77b15d1c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerSetNoCovered'] = pydantic.Field(
        'types.StickerSetNoCovered',
        alias='_'
    )

    set: "base.StickerSet"
