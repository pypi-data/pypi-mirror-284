from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LeaveChannel(BaseModel):
    """
    functions.channels.LeaveChannel
    ID: 0xf836aa95
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.LeaveChannel'] = pydantic.Field(
        'functions.channels.LeaveChannel',
        alias='_'
    )

    channel: "base.InputChannel"
