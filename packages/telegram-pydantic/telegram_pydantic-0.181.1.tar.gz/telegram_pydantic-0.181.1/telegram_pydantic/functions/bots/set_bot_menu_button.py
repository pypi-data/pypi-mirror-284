from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotMenuButton(BaseModel):
    """
    functions.bots.SetBotMenuButton
    ID: 0x4504d54f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.SetBotMenuButton'] = pydantic.Field(
        'functions.bots.SetBotMenuButton',
        alias='_'
    )

    user_id: "base.InputUser"
    button: "base.BotMenuButton"
