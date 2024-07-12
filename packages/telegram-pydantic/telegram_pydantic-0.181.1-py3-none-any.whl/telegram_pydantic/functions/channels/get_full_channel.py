from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFullChannel(BaseModel):
    """
    functions.channels.GetFullChannel
    ID: 0x8736a09
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetFullChannel'] = pydantic.Field(
        'functions.channels.GetFullChannel',
        alias='_'
    )

    channel: "base.InputChannel"
