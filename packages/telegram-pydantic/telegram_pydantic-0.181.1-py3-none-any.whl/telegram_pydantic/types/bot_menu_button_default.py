from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotMenuButtonDefault(BaseModel):
    """
    types.BotMenuButtonDefault
    ID: 0x7533a588
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotMenuButtonDefault'] = pydantic.Field(
        'types.BotMenuButtonDefault',
        alias='_'
    )

