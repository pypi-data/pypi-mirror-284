from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedChatInvite(BaseModel):
    """
    types.messages.ExportedChatInvite
    ID: 0x1871be50
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ExportedChatInvite'] = pydantic.Field(
        'types.messages.ExportedChatInvite',
        alias='_'
    )

    invite: "base.ExportedChatInvite"
    users: list["base.User"]
