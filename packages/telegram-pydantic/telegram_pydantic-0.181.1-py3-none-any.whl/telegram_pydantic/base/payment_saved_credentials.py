from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PaymentSavedCredentials - Layer 181
PaymentSavedCredentials = typing.Annotated[
    typing.Union[
        types.PaymentSavedCredentialsCard
    ],
    pydantic.Field(discriminator='QUALNAME')
]
