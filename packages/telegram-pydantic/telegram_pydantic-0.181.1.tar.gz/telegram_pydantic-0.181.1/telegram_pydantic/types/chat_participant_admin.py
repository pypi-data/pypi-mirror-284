from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatParticipantAdmin(BaseModel):
    """
    types.ChatParticipantAdmin
    ID: 0xa0933f5b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatParticipantAdmin'] = pydantic.Field(
        'types.ChatParticipantAdmin',
        alias='_'
    )

    user_id: int
    inviter_id: int
    date: int
