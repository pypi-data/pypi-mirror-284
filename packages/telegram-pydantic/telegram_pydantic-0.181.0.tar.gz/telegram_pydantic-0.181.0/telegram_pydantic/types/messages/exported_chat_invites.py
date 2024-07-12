from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedChatInvites(BaseModel):
    """
    types.messages.ExportedChatInvites
    ID: 0xbdc62dcc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ExportedChatInvites'] = pydantic.Field(
        'types.messages.ExportedChatInvites',
        alias='_'
    )

    count: int
    invites: list["base.ExportedChatInvite"]
    users: list["base.User"]
