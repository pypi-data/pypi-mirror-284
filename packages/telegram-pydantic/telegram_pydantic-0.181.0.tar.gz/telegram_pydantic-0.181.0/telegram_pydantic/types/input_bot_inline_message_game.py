from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineMessageGame(BaseModel):
    """
    types.InputBotInlineMessageGame
    ID: 0x4b425864
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineMessageGame'] = pydantic.Field(
        'types.InputBotInlineMessageGame',
        alias='_'
    )

    reply_markup: typing.Optional["base.ReplyMarkup"] = None
