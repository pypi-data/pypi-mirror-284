from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteExportedChatInvite(BaseModel):
    """
    functions.messages.DeleteExportedChatInvite
    ID: 0xd464a42b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteExportedChatInvite'] = pydantic.Field(
        'functions.messages.DeleteExportedChatInvite',
        alias='_'
    )

    peer: "base.InputPeer"
    link: str
