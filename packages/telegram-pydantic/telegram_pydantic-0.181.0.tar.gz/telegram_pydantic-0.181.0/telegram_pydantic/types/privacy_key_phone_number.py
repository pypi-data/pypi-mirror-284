from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyPhoneNumber(BaseModel):
    """
    types.PrivacyKeyPhoneNumber
    ID: 0xd19ae46d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyPhoneNumber'] = pydantic.Field(
        'types.PrivacyKeyPhoneNumber',
        alias='_'
    )

