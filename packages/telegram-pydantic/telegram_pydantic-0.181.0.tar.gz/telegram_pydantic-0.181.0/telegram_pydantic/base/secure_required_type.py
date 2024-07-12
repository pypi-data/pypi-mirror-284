from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecureRequiredType - Layer 181
SecureRequiredType = typing.Annotated[
    typing.Union[
        types.SecureRequiredType,
        types.SecureRequiredTypeOneOf
    ],
    pydantic.Field(discriminator='QUALNAME')
]
