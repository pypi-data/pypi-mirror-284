from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyPhoneP2P(BaseModel):
    """
    types.InputPrivacyKeyPhoneP2P
    ID: 0xdb9e70d2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyPhoneP2P'] = pydantic.Field(
        'types.InputPrivacyKeyPhoneP2P',
        alias='_'
    )

