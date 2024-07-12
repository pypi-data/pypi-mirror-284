from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaAreaChannelPost(BaseModel):
    """
    types.InputMediaAreaChannelPost
    ID: 0x2271f2bf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaAreaChannelPost'] = pydantic.Field(
        'types.InputMediaAreaChannelPost',
        alias='_'
    )

    coordinates: "base.MediaAreaCoordinates"
    channel: "base.InputChannel"
    msg_id: int
