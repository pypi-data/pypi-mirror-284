from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInfo(BaseModel):
    """
    types.bots.BotInfo
    ID: 0xe8a775b0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.bots.BotInfo'] = pydantic.Field(
        'types.bots.BotInfo',
        alias='_'
    )

    name: str
    about: str
    description: str
