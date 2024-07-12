from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStorePaymentPremiumGiveaway(BaseModel):
    """
    types.InputStorePaymentPremiumGiveaway
    ID: 0x160544ca
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStorePaymentPremiumGiveaway'] = pydantic.Field(
        'types.InputStorePaymentPremiumGiveaway',
        alias='_'
    )

    boost_peer: "base.InputPeer"
    random_id: int
    until_date: int
    currency: str
    amount: int
    only_new_subscribers: typing.Optional[bool] = None
    winners_are_visible: typing.Optional[bool] = None
    additional_peers: typing.Optional[list["base.InputPeer"]] = None
    countries_iso2: typing.Optional[list[str]] = None
    prize_description: typing.Optional[str] = None
