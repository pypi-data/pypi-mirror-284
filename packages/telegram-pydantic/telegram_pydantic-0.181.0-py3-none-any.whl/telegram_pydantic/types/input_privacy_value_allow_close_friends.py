from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueAllowCloseFriends(BaseModel):
    """
    types.InputPrivacyValueAllowCloseFriends
    ID: 0x2f453e49
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueAllowCloseFriends'] = pydantic.Field(
        'types.InputPrivacyValueAllowCloseFriends',
        alias='_'
    )

