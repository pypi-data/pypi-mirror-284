from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AssignAppStoreTransaction(BaseModel):
    """
    functions.payments.AssignAppStoreTransaction
    ID: 0x80ed747d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.AssignAppStoreTransaction'] = pydantic.Field(
        'functions.payments.AssignAppStoreTransaction',
        alias='_'
    )

    receipt: bytes
    purpose: "base.InputStorePaymentPurpose"
