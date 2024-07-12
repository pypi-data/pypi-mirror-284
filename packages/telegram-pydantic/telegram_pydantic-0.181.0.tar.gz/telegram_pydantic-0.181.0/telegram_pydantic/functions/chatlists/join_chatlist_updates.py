from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JoinChatlistUpdates(BaseModel):
    """
    functions.chatlists.JoinChatlistUpdates
    ID: 0xe089f8f5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.JoinChatlistUpdates'] = pydantic.Field(
        'functions.chatlists.JoinChatlistUpdates',
        alias='_'
    )

    chatlist: "base.InputChatlist"
    peers: list["base.InputPeer"]
