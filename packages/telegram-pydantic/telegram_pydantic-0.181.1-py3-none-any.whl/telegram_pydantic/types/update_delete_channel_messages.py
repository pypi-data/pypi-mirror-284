from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDeleteChannelMessages(BaseModel):
    """
    types.UpdateDeleteChannelMessages
    ID: 0xc32d5b12
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDeleteChannelMessages'] = pydantic.Field(
        'types.UpdateDeleteChannelMessages',
        alias='_'
    )

    channel_id: int
    messages: list[int]
    pts: int
    pts_count: int
