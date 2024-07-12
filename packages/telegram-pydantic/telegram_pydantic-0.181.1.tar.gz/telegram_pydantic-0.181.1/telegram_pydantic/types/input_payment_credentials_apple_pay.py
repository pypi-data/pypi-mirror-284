from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPaymentCredentialsApplePay(BaseModel):
    """
    types.InputPaymentCredentialsApplePay
    ID: 0xaa1c39f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPaymentCredentialsApplePay'] = pydantic.Field(
        'types.InputPaymentCredentialsApplePay',
        alias='_'
    )

    payment_data: "base.DataJSON"
