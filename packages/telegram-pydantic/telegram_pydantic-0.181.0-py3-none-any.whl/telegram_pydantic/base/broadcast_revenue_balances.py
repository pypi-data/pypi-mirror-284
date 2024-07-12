from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BroadcastRevenueBalances - Layer 181
BroadcastRevenueBalances = typing.Annotated[
    typing.Union[
        types.BroadcastRevenueBalances
    ],
    pydantic.Field(discriminator='QUALNAME')
]
