from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionStopPoll(BaseModel):
    """
    types.ChannelAdminLogEventActionStopPoll
    ID: 0x8f079643
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionStopPoll'] = pydantic.Field(
        'types.ChannelAdminLogEventActionStopPoll',
        alias='_'
    )

    message: "base.Message"
