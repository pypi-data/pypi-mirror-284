from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CanSendMessage(BaseModel):
    """
    functions.bots.CanSendMessage
    ID: 0x1359f4e6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.CanSendMessage'] = pydantic.Field(
        'functions.bots.CanSendMessage',
        alias='_'
    )

    bot: "base.InputUser"
