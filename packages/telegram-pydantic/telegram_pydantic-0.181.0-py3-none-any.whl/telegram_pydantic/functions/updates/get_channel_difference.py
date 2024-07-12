from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChannelDifference(BaseModel):
    """
    functions.updates.GetChannelDifference
    ID: 0x3173d78
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.updates.GetChannelDifference'] = pydantic.Field(
        'functions.updates.GetChannelDifference',
        alias='_'
    )

    channel: "base.InputChannel"
    filter: "base.ChannelMessagesFilter"
    pts: int
    limit: int
    force: typing.Optional[bool] = None
