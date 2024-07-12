from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatAdminsWithInvites(BaseModel):
    """
    types.messages.ChatAdminsWithInvites
    ID: 0xb69b72d7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ChatAdminsWithInvites'] = pydantic.Field(
        'types.messages.ChatAdminsWithInvites',
        alias='_'
    )

    admins: list["base.ChatAdminWithInvites"]
    users: list["base.User"]
