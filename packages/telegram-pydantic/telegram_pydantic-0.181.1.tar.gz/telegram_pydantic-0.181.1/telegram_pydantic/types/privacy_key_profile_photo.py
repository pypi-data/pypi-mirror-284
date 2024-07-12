from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyProfilePhoto(BaseModel):
    """
    types.PrivacyKeyProfilePhoto
    ID: 0x96151fed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyProfilePhoto'] = pydantic.Field(
        'types.PrivacyKeyProfilePhoto',
        alias='_'
    )

