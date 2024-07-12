from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PaymentRequestedInfo - Layer 181
PaymentRequestedInfo = typing.Annotated[
    typing.Union[
        types.PaymentRequestedInfo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
