from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyPhoneP2P(BaseModel):
    """
    types.PrivacyKeyPhoneP2P
    ID: 0x39491cc8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyPhoneP2P'] = pydantic.Field(
        'types.PrivacyKeyPhoneP2P',
        alias='_'
    )

