from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBroadcastRevenueWithdrawalUrl(BaseModel):
    """
    functions.stats.GetBroadcastRevenueWithdrawalUrl
    ID: 0x2a65ef73
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetBroadcastRevenueWithdrawalUrl'] = pydantic.Field(
        'functions.stats.GetBroadcastRevenueWithdrawalUrl',
        alias='_'
    )

    channel: "base.InputChannel"
    password: "base.InputCheckPasswordSRP"
