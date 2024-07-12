from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePeerWallpaper(BaseModel):
    """
    types.UpdatePeerWallpaper
    ID: 0xae3f101d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePeerWallpaper'] = pydantic.Field(
        'types.UpdatePeerWallpaper',
        alias='_'
    )

    peer: "base.Peer"
    wallpaper_overridden: typing.Optional[bool] = None
    wallpaper: typing.Optional["base.WallPaper"] = None
