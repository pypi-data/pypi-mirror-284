from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatParticipant(BaseModel):
    """
    types.ChatParticipant
    ID: 0xc02d4007
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatParticipant'] = pydantic.Field(
        'types.ChatParticipant',
        alias='_'
    )

    user_id: int
    inviter_id: int
    date: int
