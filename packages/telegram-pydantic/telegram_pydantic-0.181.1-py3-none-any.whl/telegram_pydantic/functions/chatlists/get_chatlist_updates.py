from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChatlistUpdates(BaseModel):
    """
    functions.chatlists.GetChatlistUpdates
    ID: 0x89419521
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.GetChatlistUpdates'] = pydantic.Field(
        'functions.chatlists.GetChatlistUpdates',
        alias='_'
    )

    chatlist: "base.InputChatlist"
