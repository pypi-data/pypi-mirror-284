from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueAllowPremium(BaseModel):
    """
    types.PrivacyValueAllowPremium
    ID: 0xece9814b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueAllowPremium'] = pydantic.Field(
        'types.PrivacyValueAllowPremium',
        alias='_'
    )

