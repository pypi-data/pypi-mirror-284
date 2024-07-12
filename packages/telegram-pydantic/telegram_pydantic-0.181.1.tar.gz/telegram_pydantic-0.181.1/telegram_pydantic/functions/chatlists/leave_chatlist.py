from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LeaveChatlist(BaseModel):
    """
    functions.chatlists.LeaveChatlist
    ID: 0x74fae13a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.LeaveChatlist'] = pydantic.Field(
        'functions.chatlists.LeaveChatlist',
        alias='_'
    )

    chatlist: "base.InputChatlist"
    peers: list["base.InputPeer"]
