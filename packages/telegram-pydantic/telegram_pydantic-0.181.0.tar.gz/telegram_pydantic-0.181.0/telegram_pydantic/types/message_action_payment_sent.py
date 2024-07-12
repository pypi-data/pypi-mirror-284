from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionPaymentSent(BaseModel):
    """
    types.MessageActionPaymentSent
    ID: 0x96163f56
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionPaymentSent'] = pydantic.Field(
        'types.MessageActionPaymentSent',
        alias='_'
    )

    currency: str
    total_amount: int
    recurring_init: typing.Optional[bool] = None
    recurring_used: typing.Optional[bool] = None
    invoice_slug: typing.Optional[str] = None
