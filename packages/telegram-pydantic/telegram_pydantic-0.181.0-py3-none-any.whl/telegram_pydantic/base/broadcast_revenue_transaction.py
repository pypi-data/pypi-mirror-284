from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BroadcastRevenueTransaction - Layer 181
BroadcastRevenueTransaction = typing.Annotated[
    typing.Union[
        types.BroadcastRevenueTransactionProceeds,
        types.BroadcastRevenueTransactionRefund,
        types.BroadcastRevenueTransactionWithdrawal
    ],
    pydantic.Field(discriminator='QUALNAME')
]
