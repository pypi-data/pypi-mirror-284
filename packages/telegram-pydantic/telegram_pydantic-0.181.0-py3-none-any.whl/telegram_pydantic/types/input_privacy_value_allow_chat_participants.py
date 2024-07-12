from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueAllowChatParticipants(BaseModel):
    """
    types.InputPrivacyValueAllowChatParticipants
    ID: 0x840649cf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueAllowChatParticipants'] = pydantic.Field(
        'types.InputPrivacyValueAllowChatParticipants',
        alias='_'
    )

    chats: list[int]
