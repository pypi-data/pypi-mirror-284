from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatInvitePublicJoinRequests(BaseModel):
    """
    types.ChatInvitePublicJoinRequests
    ID: 0xed107ab7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatInvitePublicJoinRequests'] = pydantic.Field(
        'types.ChatInvitePublicJoinRequests',
        alias='_'
    )

