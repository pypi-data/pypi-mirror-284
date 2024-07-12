from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGiftCode(BaseModel):
    """
    types.MessageActionGiftCode
    ID: 0x678c2e09
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGiftCode'] = pydantic.Field(
        'types.MessageActionGiftCode',
        alias='_'
    )

    months: int
    slug: str
    via_giveaway: typing.Optional[bool] = None
    unclaimed: typing.Optional[bool] = None
    boost_peer: typing.Optional["base.Peer"] = None
    currency: typing.Optional[str] = None
    amount: typing.Optional[int] = None
    crypto_currency: typing.Optional[str] = None
    crypto_amount: typing.Optional[int] = None
