from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendScreenshotNotification(BaseModel):
    """
    functions.messages.SendScreenshotNotification
    ID: 0xa1405817
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendScreenshotNotification'] = pydantic.Field(
        'functions.messages.SendScreenshotNotification',
        alias='_'
    )

    peer: "base.InputPeer"
    reply_to: "base.InputReplyTo"
    random_id: int
