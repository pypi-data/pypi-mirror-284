from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeWallpaper(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeWallpaper
    ID: 0x31bb5d52
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeWallpaper'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeWallpaper',
        alias='_'
    )

    prev_value: "base.WallPaper"
    new_value: "base.WallPaper"
