from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PremiumGiftOption - Layer 181
PremiumGiftOption = typing.Annotated[
    typing.Union[
        types.PremiumGiftOption
    ],
    pydantic.Field(discriminator='QUALNAME')
]
