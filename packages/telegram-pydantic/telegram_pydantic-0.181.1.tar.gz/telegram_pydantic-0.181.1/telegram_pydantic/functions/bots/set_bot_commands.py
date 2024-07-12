from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotCommands(BaseModel):
    """
    functions.bots.SetBotCommands
    ID: 0x517165a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.SetBotCommands'] = pydantic.Field(
        'functions.bots.SetBotCommands',
        alias='_'
    )

    scope: "base.BotCommandScope"
    lang_code: str
    commands: list["base.BotCommand"]
