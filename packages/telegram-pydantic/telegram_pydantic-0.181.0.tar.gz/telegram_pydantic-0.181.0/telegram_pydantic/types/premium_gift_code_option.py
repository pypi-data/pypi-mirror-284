from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PremiumGiftCodeOption(BaseModel):
    """
    types.PremiumGiftCodeOption
    ID: 0x257e962b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PremiumGiftCodeOption'] = pydantic.Field(
        'types.PremiumGiftCodeOption',
        alias='_'
    )

    users: int
    months: int
    currency: str
    amount: int
    store_product: typing.Optional[str] = None
    store_quantity: typing.Optional[int] = None
