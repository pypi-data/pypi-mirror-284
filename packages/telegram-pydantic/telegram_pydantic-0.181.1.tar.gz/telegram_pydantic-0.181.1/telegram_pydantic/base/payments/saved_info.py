from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# payments.SavedInfo - Layer 181
SavedInfo = typing.Annotated[
    typing.Union[
        types.payments.SavedInfo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
