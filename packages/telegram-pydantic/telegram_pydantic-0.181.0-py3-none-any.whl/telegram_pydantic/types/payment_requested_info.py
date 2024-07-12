from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentRequestedInfo(BaseModel):
    """
    types.PaymentRequestedInfo
    ID: 0x909c3f94
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PaymentRequestedInfo'] = pydantic.Field(
        'types.PaymentRequestedInfo',
        alias='_'
    )

    name: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    email: typing.Optional[str] = None
    shipping_address: typing.Optional["base.PostAddress"] = None
