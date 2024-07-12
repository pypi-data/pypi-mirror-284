from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotChatInviteRequester(BaseModel):
    """
    types.UpdateBotChatInviteRequester
    ID: 0x11dfa986
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotChatInviteRequester'] = pydantic.Field(
        'types.UpdateBotChatInviteRequester',
        alias='_'
    )

    peer: "base.Peer"
    date: int
    user_id: int
    about: str
    invite: "base.ExportedChatInvite"
    qts: int
