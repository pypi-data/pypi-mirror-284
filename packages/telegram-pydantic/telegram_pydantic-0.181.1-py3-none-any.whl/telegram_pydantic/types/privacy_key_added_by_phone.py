from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyAddedByPhone(BaseModel):
    """
    types.PrivacyKeyAddedByPhone
    ID: 0x42ffd42b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyAddedByPhone'] = pydantic.Field(
        'types.PrivacyKeyAddedByPhone',
        alias='_'
    )

