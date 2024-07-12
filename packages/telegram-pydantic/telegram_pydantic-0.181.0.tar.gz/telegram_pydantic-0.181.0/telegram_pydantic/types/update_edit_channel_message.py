from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateEditChannelMessage(BaseModel):
    """
    types.UpdateEditChannelMessage
    ID: 0x1b3f4df7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateEditChannelMessage'] = pydantic.Field(
        'types.UpdateEditChannelMessage',
        alias='_'
    )

    message: "base.Message"
    pts: int
    pts_count: int
