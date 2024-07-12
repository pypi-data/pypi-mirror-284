from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopeDefault(BaseModel):
    """
    types.BotCommandScopeDefault
    ID: 0x2f6cb2ab
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopeDefault'] = pydantic.Field(
        'types.BotCommandScopeDefault',
        alias='_'
    )

