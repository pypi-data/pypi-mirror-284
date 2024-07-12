from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stats.BroadcastRevenueWithdrawalUrl - Layer 181
BroadcastRevenueWithdrawalUrl = typing.Annotated[
    typing.Union[
        types.stats.BroadcastRevenueWithdrawalUrl
    ],
    pydantic.Field(discriminator='QUALNAME')
]
