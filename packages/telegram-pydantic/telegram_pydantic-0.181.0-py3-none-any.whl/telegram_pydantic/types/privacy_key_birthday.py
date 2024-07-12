from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyBirthday(BaseModel):
    """
    types.PrivacyKeyBirthday
    ID: 0x2000a518
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyBirthday'] = pydantic.Field(
        'types.PrivacyKeyBirthday',
        alias='_'
    )

