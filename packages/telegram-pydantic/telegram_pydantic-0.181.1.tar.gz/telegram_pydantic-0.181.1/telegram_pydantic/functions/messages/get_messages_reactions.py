from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessagesReactions(BaseModel):
    """
    functions.messages.GetMessagesReactions
    ID: 0x8bba90e6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMessagesReactions'] = pydantic.Field(
        'functions.messages.GetMessagesReactions',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
