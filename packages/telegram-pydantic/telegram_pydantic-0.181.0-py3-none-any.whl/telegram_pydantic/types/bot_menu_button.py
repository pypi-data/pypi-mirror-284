from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotMenuButton(BaseModel):
    """
    types.BotMenuButton
    ID: 0xc7b57ce6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotMenuButton'] = pydantic.Field(
        'types.BotMenuButton',
        alias='_'
    )

    text: str
    url: str
