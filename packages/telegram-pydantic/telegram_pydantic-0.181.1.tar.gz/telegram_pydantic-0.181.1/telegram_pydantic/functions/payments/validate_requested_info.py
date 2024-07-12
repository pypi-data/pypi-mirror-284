from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ValidateRequestedInfo(BaseModel):
    """
    functions.payments.ValidateRequestedInfo
    ID: 0xb6c8f12b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.ValidateRequestedInfo'] = pydantic.Field(
        'functions.payments.ValidateRequestedInfo',
        alias='_'
    )

    invoice: "base.InputInvoice"
    info: "base.PaymentRequestedInfo"
    save: typing.Optional[bool] = None
