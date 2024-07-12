from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleJoinToSend(BaseModel):
    """
    functions.channels.ToggleJoinToSend
    ID: 0xe4cb9580
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleJoinToSend'] = pydantic.Field(
        'functions.channels.ToggleJoinToSend',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
