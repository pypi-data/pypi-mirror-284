from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecureValue - Layer 181
SecureValue = typing.Annotated[
    typing.Union[
        types.SecureValue
    ],
    pydantic.Field(discriminator='QUALNAME')
]
