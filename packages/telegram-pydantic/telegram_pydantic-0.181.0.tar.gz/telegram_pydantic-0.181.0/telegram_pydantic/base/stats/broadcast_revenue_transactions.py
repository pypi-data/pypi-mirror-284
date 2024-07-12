from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stats.BroadcastRevenueTransactions - Layer 181
BroadcastRevenueTransactions = typing.Annotated[
    typing.Union[
        types.stats.BroadcastRevenueTransactions
    ],
    pydantic.Field(discriminator='QUALNAME')
]
