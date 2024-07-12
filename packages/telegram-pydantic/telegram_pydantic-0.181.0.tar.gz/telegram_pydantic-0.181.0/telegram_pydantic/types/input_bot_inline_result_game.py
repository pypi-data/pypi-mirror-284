from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineResultGame(BaseModel):
    """
    types.InputBotInlineResultGame
    ID: 0x4fa417f2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineResultGame'] = pydantic.Field(
        'types.InputBotInlineResultGame',
        alias='_'
    )

    id: str
    short_name: str
    send_message: "base.InputBotInlineMessage"
