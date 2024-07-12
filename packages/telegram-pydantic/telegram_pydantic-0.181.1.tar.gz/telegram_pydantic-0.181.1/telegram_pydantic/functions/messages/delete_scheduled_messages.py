from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteScheduledMessages(BaseModel):
    """
    functions.messages.DeleteScheduledMessages
    ID: 0x59ae2b16
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteScheduledMessages'] = pydantic.Field(
        'functions.messages.DeleteScheduledMessages',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
