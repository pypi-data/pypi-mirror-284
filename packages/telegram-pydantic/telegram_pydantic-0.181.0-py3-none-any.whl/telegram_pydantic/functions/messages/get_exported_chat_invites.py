from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetExportedChatInvites(BaseModel):
    """
    functions.messages.GetExportedChatInvites
    ID: 0xa2b5a3f6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetExportedChatInvites'] = pydantic.Field(
        'functions.messages.GetExportedChatInvites',
        alias='_'
    )

    peer: "base.InputPeer"
    admin_id: "base.InputUser"
    limit: int
    revoked: typing.Optional[bool] = None
    offset_date: typing.Optional[int] = None
    offset_link: typing.Optional[str] = None
