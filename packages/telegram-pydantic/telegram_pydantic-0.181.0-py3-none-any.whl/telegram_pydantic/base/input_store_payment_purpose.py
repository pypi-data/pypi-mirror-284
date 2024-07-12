from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputStorePaymentPurpose - Layer 181
InputStorePaymentPurpose = typing.Annotated[
    typing.Union[
        types.InputStorePaymentGiftPremium,
        types.InputStorePaymentPremiumGiftCode,
        types.InputStorePaymentPremiumGiveaway,
        types.InputStorePaymentPremiumSubscription,
        types.InputStorePaymentStars
    ],
    pydantic.Field(discriminator='QUALNAME')
]
