from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyChatInvite(BaseModel):
    """
    types.InputPrivacyKeyChatInvite
    ID: 0xbdfb0426
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyChatInvite'] = pydantic.Field(
        'types.InputPrivacyKeyChatInvite',
        alias='_'
    )

