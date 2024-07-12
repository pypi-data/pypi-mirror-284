from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewStickerSet(BaseModel):
    """
    types.UpdateNewStickerSet
    ID: 0x688a30aa
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewStickerSet'] = pydantic.Field(
        'types.UpdateNewStickerSet',
        alias='_'
    )

    stickerset: "base.messages.StickerSet"
