from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatParticipantsForbidden(BaseModel):
    """
    types.ChatParticipantsForbidden
    ID: 0x8763d3e1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatParticipantsForbidden'] = pydantic.Field(
        'types.ChatParticipantsForbidden',
        alias='_'
    )

    chat_id: int
    self_participant: typing.Optional["base.ChatParticipant"] = None
