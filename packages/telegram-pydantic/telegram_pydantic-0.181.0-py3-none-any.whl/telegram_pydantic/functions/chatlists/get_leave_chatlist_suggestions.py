from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetLeaveChatlistSuggestions(BaseModel):
    """
    functions.chatlists.GetLeaveChatlistSuggestions
    ID: 0xfdbcd714
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.GetLeaveChatlistSuggestions'] = pydantic.Field(
        'functions.chatlists.GetLeaveChatlistSuggestions',
        alias='_'
    )

    chatlist: "base.InputChatlist"
