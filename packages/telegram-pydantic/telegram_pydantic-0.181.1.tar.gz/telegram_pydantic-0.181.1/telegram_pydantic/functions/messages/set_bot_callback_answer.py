from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotCallbackAnswer(BaseModel):
    """
    functions.messages.SetBotCallbackAnswer
    ID: 0xd58f130a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetBotCallbackAnswer'] = pydantic.Field(
        'functions.messages.SetBotCallbackAnswer',
        alias='_'
    )

    query_id: int
    cache_time: int
    alert: typing.Optional[bool] = None
    message: typing.Optional[str] = None
    url: typing.Optional[str] = None
