from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCall(BaseModel):
    """
    types.phone.PhoneCall
    ID: 0xec82e140
    Layer: 181
    """
    QUALNAME: typing.Literal['types.phone.PhoneCall'] = pydantic.Field(
        'types.phone.PhoneCall',
        alias='_'
    )

    phone_call: "base.PhoneCall"
    users: list["base.User"]
