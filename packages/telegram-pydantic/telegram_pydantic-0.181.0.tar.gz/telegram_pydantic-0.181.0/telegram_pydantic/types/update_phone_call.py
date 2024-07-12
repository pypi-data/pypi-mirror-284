from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePhoneCall(BaseModel):
    """
    types.UpdatePhoneCall
    ID: 0xab0f6b1e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePhoneCall'] = pydantic.Field(
        'types.UpdatePhoneCall',
        alias='_'
    )

    phone_call: "base.PhoneCall"
