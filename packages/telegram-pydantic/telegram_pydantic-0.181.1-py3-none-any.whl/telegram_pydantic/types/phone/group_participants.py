from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupParticipants(BaseModel):
    """
    types.phone.GroupParticipants
    ID: 0xf47751b6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.phone.GroupParticipants'] = pydantic.Field(
        'types.phone.GroupParticipants',
        alias='_'
    )

    count: int
    participants: list["base.GroupCallParticipant"]
    next_offset: str
    chats: list["base.Chat"]
    users: list["base.User"]
    version: int
