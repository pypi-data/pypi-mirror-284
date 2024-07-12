from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStorePaymentGiftPremium(BaseModel):
    """
    types.InputStorePaymentGiftPremium
    ID: 0x616f7fe8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStorePaymentGiftPremium'] = pydantic.Field(
        'types.InputStorePaymentGiftPremium',
        alias='_'
    )

    user_id: "base.InputUser"
    currency: str
    amount: int
