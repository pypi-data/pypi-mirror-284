from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCall(BaseModel):
    """
    types.phone.GroupCall
    ID: 0x9e727aad
    Layer: 181
    """
    QUALNAME: typing.Literal['types.phone.GroupCall'] = pydantic.Field(
        'types.phone.GroupCall',
        alias='_'
    )

    call: "base.GroupCall"
    participants: list["base.GroupCallParticipant"]
    participants_next_offset: str
    chats: list["base.Chat"]
    users: list["base.User"]
