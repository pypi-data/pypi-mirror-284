from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# payments.BankCardData - Layer 181
BankCardData = typing.Annotated[
    typing.Union[
        types.payments.BankCardData
    ],
    pydantic.Field(discriminator='QUALNAME')
]
