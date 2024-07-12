from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueAllowPremium(BaseModel):
    """
    types.InputPrivacyValueAllowPremium
    ID: 0x77cdc9f1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueAllowPremium'] = pydantic.Field(
        'types.InputPrivacyValueAllowPremium',
        alias='_'
    )

