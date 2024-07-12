from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# payments.PaymentResult - Layer 181
PaymentResult = typing.Annotated[
    typing.Union[
        types.payments.PaymentResult,
        types.payments.PaymentVerificationNeeded
    ],
    pydantic.Field(discriminator='QUALNAME')
]
