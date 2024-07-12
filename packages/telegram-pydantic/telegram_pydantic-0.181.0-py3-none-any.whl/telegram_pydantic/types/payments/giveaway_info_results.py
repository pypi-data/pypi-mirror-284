from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GiveawayInfoResults(BaseModel):
    """
    types.payments.GiveawayInfoResults
    ID: 0xcd5570
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.GiveawayInfoResults'] = pydantic.Field(
        'types.payments.GiveawayInfoResults',
        alias='_'
    )

    start_date: int
    finish_date: int
    winners_count: int
    activated_count: int
    winner: typing.Optional[bool] = None
    refunded: typing.Optional[bool] = None
    gift_code_slug: typing.Optional[str] = None
