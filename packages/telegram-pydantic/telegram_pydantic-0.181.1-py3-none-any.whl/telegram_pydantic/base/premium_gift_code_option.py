from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PremiumGiftCodeOption - Layer 181
PremiumGiftCodeOption = typing.Annotated[
    typing.Union[
        types.PremiumGiftCodeOption
    ],
    pydantic.Field(discriminator='QUALNAME')
]
