from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentFormMethod(BaseModel):
    """
    types.PaymentFormMethod
    ID: 0x88f8f21b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PaymentFormMethod'] = pydantic.Field(
        'types.PaymentFormMethod',
        alias='_'
    )

    url: str
    title: str
