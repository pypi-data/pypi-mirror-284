from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetInlineGameHighScores(BaseModel):
    """
    functions.messages.GetInlineGameHighScores
    ID: 0xf635e1b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetInlineGameHighScores'] = pydantic.Field(
        'functions.messages.GetInlineGameHighScores',
        alias='_'
    )

    id: "base.InputBotInlineMessageID"
    user_id: "base.InputUser"
