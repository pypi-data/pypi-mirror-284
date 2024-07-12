from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetScheduledMessages(BaseModel):
    """
    functions.messages.GetScheduledMessages
    ID: 0xbdbb0464
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetScheduledMessages'] = pydantic.Field(
        'functions.messages.GetScheduledMessages',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
