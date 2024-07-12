from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AssignPlayMarketTransaction(BaseModel):
    """
    functions.payments.AssignPlayMarketTransaction
    ID: 0xdffd50d3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.AssignPlayMarketTransaction'] = pydantic.Field(
        'functions.payments.AssignPlayMarketTransaction',
        alias='_'
    )

    receipt: "base.DataJSON"
    purpose: "base.InputStorePaymentPurpose"
