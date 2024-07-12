from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PaymentCharge - Layer 181
PaymentCharge = typing.Annotated[
    typing.Union[
        types.PaymentCharge
    ],
    pydantic.Field(discriminator='QUALNAME')
]
