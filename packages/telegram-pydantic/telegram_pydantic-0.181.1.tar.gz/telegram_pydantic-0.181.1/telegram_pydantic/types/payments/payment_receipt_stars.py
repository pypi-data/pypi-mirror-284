from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentReceiptStars(BaseModel):
    """
    types.payments.PaymentReceiptStars
    ID: 0xdabbf83a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.PaymentReceiptStars'] = pydantic.Field(
        'types.payments.PaymentReceiptStars',
        alias='_'
    )

    date: int
    bot_id: int
    title: str
    description: str
    invoice: "base.Invoice"
    currency: str
    total_amount: int
    transaction_id: str
    users: list["base.User"]
    photo: typing.Optional["base.WebDocument"] = None
