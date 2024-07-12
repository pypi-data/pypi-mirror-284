from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueTransactionRefund(BaseModel):
    """
    types.BroadcastRevenueTransactionRefund
    ID: 0x42d30d2e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BroadcastRevenueTransactionRefund'] = pydantic.Field(
        'types.BroadcastRevenueTransactionRefund',
        alias='_'
    )

    amount: int
    date: int
    provider: str
