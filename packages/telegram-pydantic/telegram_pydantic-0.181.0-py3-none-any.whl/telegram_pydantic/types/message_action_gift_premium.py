from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGiftPremium(BaseModel):
    """
    types.MessageActionGiftPremium
    ID: 0xc83d6aec
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGiftPremium'] = pydantic.Field(
        'types.MessageActionGiftPremium',
        alias='_'
    )

    currency: str
    amount: int
    months: int
    crypto_currency: typing.Optional[str] = None
    crypto_amount: typing.Optional[int] = None
