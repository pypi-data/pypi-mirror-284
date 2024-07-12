from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyAddedByPhone(BaseModel):
    """
    types.InputPrivacyKeyAddedByPhone
    ID: 0xd1219bdd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyAddedByPhone'] = pydantic.Field(
        'types.InputPrivacyKeyAddedByPhone',
        alias='_'
    )

