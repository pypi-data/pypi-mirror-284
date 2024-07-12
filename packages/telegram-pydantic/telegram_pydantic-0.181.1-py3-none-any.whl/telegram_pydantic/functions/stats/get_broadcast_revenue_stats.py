from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBroadcastRevenueStats(BaseModel):
    """
    functions.stats.GetBroadcastRevenueStats
    ID: 0x75dfb671
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetBroadcastRevenueStats'] = pydantic.Field(
        'functions.stats.GetBroadcastRevenueStats',
        alias='_'
    )

    channel: "base.InputChannel"
    dark: typing.Optional[bool] = None
