from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedInvites(BaseModel):
    """
    types.chatlists.ExportedInvites
    ID: 0x10ab6dc7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.chatlists.ExportedInvites'] = pydantic.Field(
        'types.chatlists.ExportedInvites',
        alias='_'
    )

    invites: list["base.ExportedChatlistInvite"]
    chats: list["base.Chat"]
    users: list["base.User"]
