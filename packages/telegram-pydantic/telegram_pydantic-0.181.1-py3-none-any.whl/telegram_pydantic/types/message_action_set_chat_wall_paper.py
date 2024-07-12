from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionSetChatWallPaper(BaseModel):
    """
    types.MessageActionSetChatWallPaper
    ID: 0x5060a3f4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionSetChatWallPaper'] = pydantic.Field(
        'types.MessageActionSetChatWallPaper',
        alias='_'
    )

    wallpaper: "base.WallPaper"
    same: typing.Optional[bool] = None
    for_both: typing.Optional[bool] = None
