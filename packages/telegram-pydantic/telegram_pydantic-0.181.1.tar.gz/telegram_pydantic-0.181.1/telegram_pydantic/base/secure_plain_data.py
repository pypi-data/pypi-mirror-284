from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecurePlainData - Layer 181
SecurePlainData = typing.Annotated[
    typing.Union[
        types.SecurePlainEmail,
        types.SecurePlainPhone
    ],
    pydantic.Field(discriminator='QUALNAME')
]
