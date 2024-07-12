from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# payments.PaymentReceipt - Layer 181
PaymentReceipt = typing.Annotated[
    typing.Union[
        types.payments.PaymentReceipt,
        types.payments.PaymentReceiptStars
    ],
    pydantic.Field(discriminator='QUALNAME')
]
