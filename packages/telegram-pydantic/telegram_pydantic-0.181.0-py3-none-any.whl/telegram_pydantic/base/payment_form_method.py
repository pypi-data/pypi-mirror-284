from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PaymentFormMethod - Layer 181
PaymentFormMethod = typing.Annotated[
    typing.Union[
        types.PaymentFormMethod
    ],
    pydantic.Field(discriminator='QUALNAME')
]
