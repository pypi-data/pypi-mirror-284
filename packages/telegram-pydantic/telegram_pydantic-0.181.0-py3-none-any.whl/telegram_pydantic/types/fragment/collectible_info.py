from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CollectibleInfo(BaseModel):
    """
    types.fragment.CollectibleInfo
    ID: 0x6ebdff91
    Layer: 181
    """
    QUALNAME: typing.Literal['types.fragment.CollectibleInfo'] = pydantic.Field(
        'types.fragment.CollectibleInfo',
        alias='_'
    )

    purchase_date: int
    currency: str
    amount: int
    crypto_currency: str
    crypto_amount: int
    url: str
