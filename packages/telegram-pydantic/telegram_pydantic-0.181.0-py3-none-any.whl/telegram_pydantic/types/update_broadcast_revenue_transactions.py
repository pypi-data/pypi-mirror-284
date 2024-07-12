from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBroadcastRevenueTransactions(BaseModel):
    """
    types.UpdateBroadcastRevenueTransactions
    ID: 0xdfd961f5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBroadcastRevenueTransactions'] = pydantic.Field(
        'types.UpdateBroadcastRevenueTransactions',
        alias='_'
    )

    peer: "base.Peer"
    balances: "base.BroadcastRevenueBalances"
