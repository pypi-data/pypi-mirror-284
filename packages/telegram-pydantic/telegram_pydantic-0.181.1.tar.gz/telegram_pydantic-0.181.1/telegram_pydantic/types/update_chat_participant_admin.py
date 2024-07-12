from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChatParticipantAdmin(BaseModel):
    """
    types.UpdateChatParticipantAdmin
    ID: 0xd7ca61a2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChatParticipantAdmin'] = pydantic.Field(
        'types.UpdateChatParticipantAdmin',
        alias='_'
    )

    chat_id: int
    user_id: int
    is_admin: bool
    version: int
