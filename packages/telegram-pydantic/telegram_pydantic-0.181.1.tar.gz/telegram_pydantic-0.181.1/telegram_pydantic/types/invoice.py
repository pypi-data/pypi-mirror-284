from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Invoice(BaseModel):
    """
    types.Invoice
    ID: 0x5db95a15
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Invoice'] = pydantic.Field(
        'types.Invoice',
        alias='_'
    )

    currency: str
    prices: list["base.LabeledPrice"]
    test: typing.Optional[bool] = None
    name_requested: typing.Optional[bool] = None
    phone_requested: typing.Optional[bool] = None
    email_requested: typing.Optional[bool] = None
    shipping_address_requested: typing.Optional[bool] = None
    flexible: typing.Optional[bool] = None
    phone_to_provider: typing.Optional[bool] = None
    email_to_provider: typing.Optional[bool] = None
    recurring: typing.Optional[bool] = None
    max_tip_amount: typing.Optional[int] = None
    suggested_tip_amounts: typing.Optional[list[int]] = None
    terms_url: typing.Optional[str] = None
