from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AllowSendMessage(BaseModel):
    """
    functions.bots.AllowSendMessage
    ID: 0xf132e3ef
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.AllowSendMessage'] = pydantic.Field(
        'functions.bots.AllowSendMessage',
        alias='_'
    )

    bot: "base.InputUser"
