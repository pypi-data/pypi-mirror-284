from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyPhoneNumber(BaseModel):
    """
    types.InputPrivacyKeyPhoneNumber
    ID: 0x352dafa
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyPhoneNumber'] = pydantic.Field(
        'types.InputPrivacyKeyPhoneNumber',
        alias='_'
    )

