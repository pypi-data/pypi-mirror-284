from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InviteToChannel(BaseModel):
    """
    functions.channels.InviteToChannel
    ID: 0xc9e33d54
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.InviteToChannel'] = pydantic.Field(
        'functions.channels.InviteToChannel',
        alias='_'
    )

    channel: "base.InputChannel"
    users: list["base.InputUser"]
