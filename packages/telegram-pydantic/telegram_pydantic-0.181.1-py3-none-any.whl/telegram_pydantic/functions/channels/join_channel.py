from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JoinChannel(BaseModel):
    """
    functions.channels.JoinChannel
    ID: 0x24b524c5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.JoinChannel'] = pydantic.Field(
        'functions.channels.JoinChannel',
        alias='_'
    )

    channel: "base.InputChannel"
