from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedChatInviteReplaced(BaseModel):
    """
    types.messages.ExportedChatInviteReplaced
    ID: 0x222600ef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ExportedChatInviteReplaced'] = pydantic.Field(
        'types.messages.ExportedChatInviteReplaced',
        alias='_'
    )

    invite: "base.ExportedChatInvite"
    new_invite: "base.ExportedChatInvite"
    users: list["base.User"]
