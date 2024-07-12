from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyPhoneCall(BaseModel):
    """
    types.InputPrivacyKeyPhoneCall
    ID: 0xfabadc5f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyPhoneCall'] = pydantic.Field(
        'types.InputPrivacyKeyPhoneCall',
        alias='_'
    )

