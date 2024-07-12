from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestAppWebView(BaseModel):
    """
    functions.messages.RequestAppWebView
    ID: 0x8c5a3b3c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.RequestAppWebView'] = pydantic.Field(
        'functions.messages.RequestAppWebView',
        alias='_'
    )

    peer: "base.InputPeer"
    app: "base.InputBotApp"
    platform: str
    write_allowed: typing.Optional[bool] = None
    start_param: typing.Optional[str] = None
    theme_params: typing.Optional["base.DataJSON"] = None
