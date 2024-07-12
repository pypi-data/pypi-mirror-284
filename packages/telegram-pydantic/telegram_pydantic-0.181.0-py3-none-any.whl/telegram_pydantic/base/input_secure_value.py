from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputSecureValue - Layer 181
InputSecureValue = typing.Annotated[
    typing.Union[
        types.InputSecureValue
    ],
    pydantic.Field(discriminator='QUALNAME')
]
