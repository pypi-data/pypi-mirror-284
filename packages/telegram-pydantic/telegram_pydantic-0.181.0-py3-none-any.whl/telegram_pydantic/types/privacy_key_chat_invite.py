from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyChatInvite(BaseModel):
    """
    types.PrivacyKeyChatInvite
    ID: 0x500e6dfa
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyChatInvite'] = pydantic.Field(
        'types.PrivacyKeyChatInvite',
        alias='_'
    )

