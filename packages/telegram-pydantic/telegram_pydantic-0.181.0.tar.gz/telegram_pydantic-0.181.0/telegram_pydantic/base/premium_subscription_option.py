from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PremiumSubscriptionOption - Layer 181
PremiumSubscriptionOption = typing.Annotated[
    typing.Union[
        types.PremiumSubscriptionOption
    ],
    pydantic.Field(discriminator='QUALNAME')
]
