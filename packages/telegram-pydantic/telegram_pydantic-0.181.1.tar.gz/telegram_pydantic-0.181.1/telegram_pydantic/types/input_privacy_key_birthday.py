from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyBirthday(BaseModel):
    """
    types.InputPrivacyKeyBirthday
    ID: 0xd65a11cc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyBirthday'] = pydantic.Field(
        'types.InputPrivacyKeyBirthday',
        alias='_'
    )

