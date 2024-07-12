from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotCommands(BaseModel):
    """
    types.UpdateBotCommands
    ID: 0x4d712f2e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotCommands'] = pydantic.Field(
        'types.UpdateBotCommands',
        alias='_'
    )

    peer: "base.Peer"
    bot_id: int
    commands: list["base.BotCommand"]
