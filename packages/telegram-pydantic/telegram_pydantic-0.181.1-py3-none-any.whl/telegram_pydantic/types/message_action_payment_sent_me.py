from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionPaymentSentMe(BaseModel):
    """
    types.MessageActionPaymentSentMe
    ID: 0x8f31b327
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionPaymentSentMe'] = pydantic.Field(
        'types.MessageActionPaymentSentMe',
        alias='_'
    )

    currency: str
    total_amount: int
    payload: bytes
    charge: "base.PaymentCharge"
    recurring_init: typing.Optional[bool] = None
    recurring_used: typing.Optional[bool] = None
    info: typing.Optional["base.PaymentRequestedInfo"] = None
    shipping_option_id: typing.Optional[str] = None
