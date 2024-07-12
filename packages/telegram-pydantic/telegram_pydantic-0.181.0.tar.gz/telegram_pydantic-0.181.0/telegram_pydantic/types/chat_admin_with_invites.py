from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatAdminWithInvites(BaseModel):
    """
    types.ChatAdminWithInvites
    ID: 0xf2ecef23
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatAdminWithInvites'] = pydantic.Field(
        'types.ChatAdminWithInvites',
        alias='_'
    )

    admin_id: int
    invites_count: int
    revoked_invites_count: int
