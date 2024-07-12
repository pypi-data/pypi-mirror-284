from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrlStickerSet(BaseModel):
    """
    types.RecentMeUrlStickerSet
    ID: 0xbc0a57dc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RecentMeUrlStickerSet'] = pydantic.Field(
        'types.RecentMeUrlStickerSet',
        alias='_'
    )

    url: str
    set: "base.StickerSetCovered"
