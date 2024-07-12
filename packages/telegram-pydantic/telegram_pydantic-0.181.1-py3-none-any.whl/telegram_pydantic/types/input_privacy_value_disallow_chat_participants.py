from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueDisallowChatParticipants(BaseModel):
    """
    types.InputPrivacyValueDisallowChatParticipants
    ID: 0xe94f0f86
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueDisallowChatParticipants'] = pydantic.Field(
        'types.InputPrivacyValueDisallowChatParticipants',
        alias='_'
    )

    chats: list[int]
