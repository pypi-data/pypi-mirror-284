from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotMenuButtonCommands(BaseModel):
    """
    types.BotMenuButtonCommands
    ID: 0x4258c205
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotMenuButtonCommands'] = pydantic.Field(
        'types.BotMenuButtonCommands',
        alias='_'
    )

