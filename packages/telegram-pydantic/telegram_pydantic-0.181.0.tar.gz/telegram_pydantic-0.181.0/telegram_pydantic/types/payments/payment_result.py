from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentResult(BaseModel):
    """
    types.payments.PaymentResult
    ID: 0x4e5f810d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.PaymentResult'] = pydantic.Field(
        'types.payments.PaymentResult',
        alias='_'
    )

    updates: "base.Updates"
