from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendQuickReplyMessages(BaseModel):
    """
    functions.messages.SendQuickReplyMessages
    ID: 0x6c750de1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendQuickReplyMessages'] = pydantic.Field(
        'functions.messages.SendQuickReplyMessages',
        alias='_'
    )

    peer: "base.InputPeer"
    shortcut_id: int
    id: list[int]
    random_id: list[int]
