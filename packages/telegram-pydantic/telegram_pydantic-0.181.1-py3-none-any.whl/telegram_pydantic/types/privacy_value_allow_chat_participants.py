from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueAllowChatParticipants(BaseModel):
    """
    types.PrivacyValueAllowChatParticipants
    ID: 0x6b134e8e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueAllowChatParticipants'] = pydantic.Field(
        'types.PrivacyValueAllowChatParticipants',
        alias='_'
    )

    chats: list[int]
