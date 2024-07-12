from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPaymentReceipt(BaseModel):
    """
    functions.payments.GetPaymentReceipt
    ID: 0x2478d1cc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetPaymentReceipt'] = pydantic.Field(
        'functions.payments.GetPaymentReceipt',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
