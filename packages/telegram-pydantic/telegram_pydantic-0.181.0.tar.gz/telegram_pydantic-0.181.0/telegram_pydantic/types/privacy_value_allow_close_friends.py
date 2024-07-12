from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueAllowCloseFriends(BaseModel):
    """
    types.PrivacyValueAllowCloseFriends
    ID: 0xf7e8d89b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueAllowCloseFriends'] = pydantic.Field(
        'types.PrivacyValueAllowCloseFriends',
        alias='_'
    )

