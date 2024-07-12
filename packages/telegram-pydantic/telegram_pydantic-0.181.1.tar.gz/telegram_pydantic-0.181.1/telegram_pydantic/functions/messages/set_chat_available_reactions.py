from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetChatAvailableReactions(BaseModel):
    """
    functions.messages.SetChatAvailableReactions
    ID: 0x5a150bd4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetChatAvailableReactions'] = pydantic.Field(
        'functions.messages.SetChatAvailableReactions',
        alias='_'
    )

    peer: "base.InputPeer"
    available_reactions: "base.ChatReactions"
    reactions_limit: typing.Optional[int] = None
