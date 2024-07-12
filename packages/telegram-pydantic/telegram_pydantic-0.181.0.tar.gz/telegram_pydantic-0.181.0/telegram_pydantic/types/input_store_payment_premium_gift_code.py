from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStorePaymentPremiumGiftCode(BaseModel):
    """
    types.InputStorePaymentPremiumGiftCode
    ID: 0xa3805f3f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStorePaymentPremiumGiftCode'] = pydantic.Field(
        'types.InputStorePaymentPremiumGiftCode',
        alias='_'
    )

    users: list["base.InputUser"]
    currency: str
    amount: int
    boost_peer: typing.Optional["base.InputPeer"] = None
