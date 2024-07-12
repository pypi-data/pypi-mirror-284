from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastRevenueWithdrawalUrl(BaseModel):
    """
    types.stats.BroadcastRevenueWithdrawalUrl
    ID: 0xec659737
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.BroadcastRevenueWithdrawalUrl'] = pydantic.Field(
        'types.stats.BroadcastRevenueWithdrawalUrl',
        alias='_'
    )

    url: str
