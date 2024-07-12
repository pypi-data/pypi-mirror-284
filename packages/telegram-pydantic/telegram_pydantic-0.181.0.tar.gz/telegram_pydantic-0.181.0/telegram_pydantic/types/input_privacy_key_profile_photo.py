from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyProfilePhoto(BaseModel):
    """
    types.InputPrivacyKeyProfilePhoto
    ID: 0x5719bacc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyProfilePhoto'] = pydantic.Field(
        'types.InputPrivacyKeyProfilePhoto',
        alias='_'
    )

