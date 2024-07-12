from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetExportedChatInvite(BaseModel):
    """
    functions.messages.GetExportedChatInvite
    ID: 0x73746f5c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetExportedChatInvite'] = pydantic.Field(
        'functions.messages.GetExportedChatInvite',
        alias='_'
    )

    peer: "base.InputPeer"
    link: str
