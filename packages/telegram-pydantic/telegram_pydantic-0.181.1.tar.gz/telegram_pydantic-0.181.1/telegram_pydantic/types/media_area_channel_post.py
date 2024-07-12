from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MediaAreaChannelPost(BaseModel):
    """
    types.MediaAreaChannelPost
    ID: 0x770416af
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MediaAreaChannelPost'] = pydantic.Field(
        'types.MediaAreaChannelPost',
        alias='_'
    )

    coordinates: "base.MediaAreaCoordinates"
    channel_id: int
    msg_id: int
