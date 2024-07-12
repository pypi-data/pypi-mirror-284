from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputPaymentCredentials - Layer 181
InputPaymentCredentials = typing.Annotated[
    typing.Union[
        types.InputPaymentCredentials,
        types.InputPaymentCredentialsApplePay,
        types.InputPaymentCredentialsGooglePay,
        types.InputPaymentCredentialsSaved
    ],
    pydantic.Field(discriminator='QUALNAME')
]
