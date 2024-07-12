from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEvent(BaseModel):
    """
    types.ChannelAdminLogEvent
    ID: 0x1fad68cd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEvent'] = pydantic.Field(
        'types.ChannelAdminLogEvent',
        alias='_'
    )

    id: int
    date: int
    user_id: int
    action: "base.ChannelAdminLogEventAction"
