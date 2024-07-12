from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChatParticipants(BaseModel):
    """
    types.UpdateChatParticipants
    ID: 0x7761198
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChatParticipants'] = pydantic.Field(
        'types.UpdateChatParticipants',
        alias='_'
    )

    participants: "base.ChatParticipants"
