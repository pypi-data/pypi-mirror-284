from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBotMenuButton(BaseModel):
    """
    functions.bots.GetBotMenuButton
    ID: 0x9c60eb28
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.GetBotMenuButton'] = pydantic.Field(
        'functions.bots.GetBotMenuButton',
        alias='_'
    )

    user_id: "base.InputUser"
