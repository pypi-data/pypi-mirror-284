from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HideChatlistUpdates(BaseModel):
    """
    functions.chatlists.HideChatlistUpdates
    ID: 0x66e486fb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.HideChatlistUpdates'] = pydantic.Field(
        'functions.chatlists.HideChatlistUpdates',
        alias='_'
    )

    chatlist: "base.InputChatlist"
