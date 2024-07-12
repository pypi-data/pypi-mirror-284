from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBotInfo(BaseModel):
    """
    functions.bots.GetBotInfo
    ID: 0xdcd914fd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.GetBotInfo'] = pydantic.Field(
        'functions.bots.GetBotInfo',
        alias='_'
    )

    lang_code: str
    bot: typing.Optional["base.InputUser"] = None
