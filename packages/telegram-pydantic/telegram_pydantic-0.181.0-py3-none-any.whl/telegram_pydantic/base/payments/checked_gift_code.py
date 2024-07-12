from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# payments.CheckedGiftCode - Layer 181
CheckedGiftCode = typing.Annotated[
    typing.Union[
        types.payments.CheckedGiftCode
    ],
    pydantic.Field(discriminator='QUALNAME')
]
