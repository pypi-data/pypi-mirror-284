from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommand(BaseModel):
    """
    types.BotCommand
    ID: 0xc27ac8c7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommand'] = pydantic.Field(
        'types.BotCommand',
        alias='_'
    )

    command: str
    description: str
