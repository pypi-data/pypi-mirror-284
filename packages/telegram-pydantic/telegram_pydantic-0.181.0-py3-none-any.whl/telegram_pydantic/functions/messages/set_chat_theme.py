from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetChatTheme(BaseModel):
    """
    functions.messages.SetChatTheme
    ID: 0xe63be13f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetChatTheme'] = pydantic.Field(
        'functions.messages.SetChatTheme',
        alias='_'
    )

    peer: "base.InputPeer"
    emoticon: str
