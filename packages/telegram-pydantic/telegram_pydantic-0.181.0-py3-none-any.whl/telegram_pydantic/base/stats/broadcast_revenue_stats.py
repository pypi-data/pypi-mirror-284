from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stats.BroadcastRevenueStats - Layer 181
BroadcastRevenueStats = typing.Annotated[
    typing.Union[
        types.stats.BroadcastRevenueStats
    ],
    pydantic.Field(discriminator='QUALNAME')
]
