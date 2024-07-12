from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecureData - Layer 181
SecureData = typing.Annotated[
    typing.Union[
        types.SecureData
    ],
    pydantic.Field(discriminator='QUALNAME')
]
