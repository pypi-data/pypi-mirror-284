from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# payments.PaymentForm - Layer 181
PaymentForm = typing.Annotated[
    typing.Union[
        types.payments.PaymentForm,
        types.payments.PaymentFormStars
    ],
    pydantic.Field(discriminator='QUALNAME')
]
