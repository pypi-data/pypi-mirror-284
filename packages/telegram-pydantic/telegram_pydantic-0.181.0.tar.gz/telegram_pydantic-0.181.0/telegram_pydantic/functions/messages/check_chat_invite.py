from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckChatInvite(BaseModel):
    """
    functions.messages.CheckChatInvite
    ID: 0x3eadb1bb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.CheckChatInvite'] = pydantic.Field(
        'functions.messages.CheckChatInvite',
        alias='_'
    )

    hash: str
