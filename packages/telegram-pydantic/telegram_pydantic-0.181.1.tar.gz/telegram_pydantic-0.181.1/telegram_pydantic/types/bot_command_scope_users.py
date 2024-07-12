from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopeUsers(BaseModel):
    """
    types.BotCommandScopeUsers
    ID: 0x3c4f04d8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopeUsers'] = pydantic.Field(
        'types.BotCommandScopeUsers',
        alias='_'
    )

