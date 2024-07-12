from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueDisallowChatParticipants(BaseModel):
    """
    types.PrivacyValueDisallowChatParticipants
    ID: 0x41c87565
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueDisallowChatParticipants'] = pydantic.Field(
        'types.PrivacyValueDisallowChatParticipants',
        alias='_'
    )

    chats: list[int]
