from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueTransactionProceeds(BaseModel):
    """
    types.BroadcastRevenueTransactionProceeds
    ID: 0x557e2cc4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BroadcastRevenueTransactionProceeds'] = pydantic.Field(
        'types.BroadcastRevenueTransactionProceeds',
        alias='_'
    )

    amount: int
    from_date: int
    to_date: int
