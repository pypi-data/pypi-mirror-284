from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueTransactions(BaseModel):
    """
    types.stats.BroadcastRevenueTransactions
    ID: 0x87158466
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.BroadcastRevenueTransactions'] = pydantic.Field(
        'types.stats.BroadcastRevenueTransactions',
        alias='_'
    )

    count: int
    transactions: list["base.BroadcastRevenueTransaction"]
