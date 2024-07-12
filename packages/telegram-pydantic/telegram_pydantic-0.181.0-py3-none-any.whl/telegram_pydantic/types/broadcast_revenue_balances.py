from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueBalances(BaseModel):
    """
    types.BroadcastRevenueBalances
    ID: 0x8438f1c6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BroadcastRevenueBalances'] = pydantic.Field(
        'types.BroadcastRevenueBalances',
        alias='_'
    )

    current_balance: int
    available_balance: int
    overall_revenue: int
