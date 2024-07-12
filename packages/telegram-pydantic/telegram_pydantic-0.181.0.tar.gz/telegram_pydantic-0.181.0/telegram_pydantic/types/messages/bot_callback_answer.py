from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCallbackAnswer(BaseModel):
    """
    types.messages.BotCallbackAnswer
    ID: 0x36585ea4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.BotCallbackAnswer'] = pydantic.Field(
        'types.messages.BotCallbackAnswer',
        alias='_'
    )

    cache_time: int
    alert: typing.Optional[bool] = None
    has_url: typing.Optional[bool] = None
    native_ui: typing.Optional[bool] = None
    message: typing.Optional[str] = None
    url: typing.Optional[str] = None
