from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBotCommands(BaseModel):
    """
    functions.bots.GetBotCommands
    ID: 0xe34c0dd6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.GetBotCommands'] = pydantic.Field(
        'functions.bots.GetBotCommands',
        alias='_'
    )

    scope: "base.BotCommandScope"
    lang_code: str
