from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteRevokedExportedChatInvites(BaseModel):
    """
    functions.messages.DeleteRevokedExportedChatInvites
    ID: 0x56987bd5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteRevokedExportedChatInvites'] = pydantic.Field(
        'functions.messages.DeleteRevokedExportedChatInvites',
        alias='_'
    )

    peer: "base.InputPeer"
    admin_id: "base.InputUser"
