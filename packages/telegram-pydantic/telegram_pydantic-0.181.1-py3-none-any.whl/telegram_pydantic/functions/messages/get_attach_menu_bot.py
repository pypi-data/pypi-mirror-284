from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAttachMenuBot(BaseModel):
    """
    functions.messages.GetAttachMenuBot
    ID: 0x77216192
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAttachMenuBot'] = pydantic.Field(
        'functions.messages.GetAttachMenuBot',
        alias='_'
    )

    bot: "base.InputUser"
