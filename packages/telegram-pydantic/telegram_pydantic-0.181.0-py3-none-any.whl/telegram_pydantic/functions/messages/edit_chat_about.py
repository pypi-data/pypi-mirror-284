from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditChatAbout(BaseModel):
    """
    functions.messages.EditChatAbout
    ID: 0xdef60797
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditChatAbout'] = pydantic.Field(
        'functions.messages.EditChatAbout',
        alias='_'
    )

    peer: "base.InputPeer"
    about: str
