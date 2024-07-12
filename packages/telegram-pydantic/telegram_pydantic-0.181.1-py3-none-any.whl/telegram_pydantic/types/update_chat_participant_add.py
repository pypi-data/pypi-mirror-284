from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChatParticipantAdd(BaseModel):
    """
    types.UpdateChatParticipantAdd
    ID: 0x3dda5451
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChatParticipantAdd'] = pydantic.Field(
        'types.UpdateChatParticipantAdd',
        alias='_'
    )

    chat_id: int
    user_id: int
    inviter_id: int
    date: int
    version: int
