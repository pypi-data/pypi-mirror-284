from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ShippingOption(BaseModel):
    """
    types.ShippingOption
    ID: 0xb6213cdf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ShippingOption'] = pydantic.Field(
        'types.ShippingOption',
        alias='_'
    )

    id: str
    title: str
    prices: list["base.LabeledPrice"]
