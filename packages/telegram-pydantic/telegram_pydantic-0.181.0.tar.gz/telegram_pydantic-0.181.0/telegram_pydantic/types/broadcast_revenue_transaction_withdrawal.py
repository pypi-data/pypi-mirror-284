from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueTransactionWithdrawal(BaseModel):
    """
    types.BroadcastRevenueTransactionWithdrawal
    ID: 0x5a590978
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BroadcastRevenueTransactionWithdrawal'] = pydantic.Field(
        'types.BroadcastRevenueTransactionWithdrawal',
        alias='_'
    )

    amount: int
    date: int
    provider: str
    pending: typing.Optional[bool] = None
    failed: typing.Optional[bool] = None
    transaction_date: typing.Optional[int] = None
    transaction_url: typing.Optional[str] = None
