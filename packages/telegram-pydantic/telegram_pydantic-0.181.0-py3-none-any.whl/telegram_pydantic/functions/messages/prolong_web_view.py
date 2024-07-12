from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ProlongWebView(BaseModel):
    """
    functions.messages.ProlongWebView
    ID: 0xb0d81a83
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ProlongWebView'] = pydantic.Field(
        'functions.messages.ProlongWebView',
        alias='_'
    )

    peer: "base.InputPeer"
    bot: "base.InputUser"
    query_id: int
    silent: typing.Optional[bool] = None
    reply_to: typing.Optional["base.InputReplyTo"] = None
    send_as: typing.Optional["base.InputPeer"] = None
