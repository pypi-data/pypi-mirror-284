from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvitedUsers(BaseModel):
    """
    types.messages.InvitedUsers
    ID: 0x7f5defa6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.InvitedUsers'] = pydantic.Field(
        'types.messages.InvitedUsers',
        alias='_'
    )

    updates: "base.Updates"
    missing_invitees: list["base.MissingInvitee"]
