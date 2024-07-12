from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendWebViewResultMessage(BaseModel):
    """
    functions.messages.SendWebViewResultMessage
    ID: 0xa4314f5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendWebViewResultMessage'] = pydantic.Field(
        'functions.messages.SendWebViewResultMessage',
        alias='_'
    )

    bot_query_id: str
    result: "base.InputBotInlineResult"
