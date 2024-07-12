from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrlChatInvite(BaseModel):
    """
    types.RecentMeUrlChatInvite
    ID: 0xeb49081d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RecentMeUrlChatInvite'] = pydantic.Field(
        'types.RecentMeUrlChatInvite',
        alias='_'
    )

    url: str
    chat_invite: "base.ChatInvite"
