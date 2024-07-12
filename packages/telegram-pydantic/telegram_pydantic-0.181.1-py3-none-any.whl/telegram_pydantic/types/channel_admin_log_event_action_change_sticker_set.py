from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeStickerSet(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeStickerSet
    ID: 0xb1c3caa7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeStickerSet'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeStickerSet',
        alias='_'
    )

    prev_stickerset: "base.InputStickerSet"
    new_stickerset: "base.InputStickerSet"
