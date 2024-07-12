from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStorePaymentStars(BaseModel):
    """
    types.InputStorePaymentStars
    ID: 0x4f0ee8df
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStorePaymentStars'] = pydantic.Field(
        'types.InputStorePaymentStars',
        alias='_'
    )

    stars: int
    currency: str
    amount: int
