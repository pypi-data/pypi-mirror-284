from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBroadcastRevenueTransactions(BaseModel):
    """
    functions.stats.GetBroadcastRevenueTransactions
    ID: 0x69280f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetBroadcastRevenueTransactions'] = pydantic.Field(
        'functions.stats.GetBroadcastRevenueTransactions',
        alias='_'
    )

    channel: "base.InputChannel"
    offset: int
    limit: int
