from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChatParticipant(BaseModel):
    """
    types.UpdateChatParticipant
    ID: 0xd087663a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChatParticipant'] = pydantic.Field(
        'types.UpdateChatParticipant',
        alias='_'
    )

    chat_id: int
    date: int
    actor_id: int
    user_id: int
    qts: int
    prev_participant: typing.Optional["base.ChatParticipant"] = None
    new_participant: typing.Optional["base.ChatParticipant"] = None
    invite: typing.Optional["base.ExportedChatInvite"] = None
