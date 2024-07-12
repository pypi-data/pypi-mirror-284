from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecureCredentialsEncrypted - Layer 181
SecureCredentialsEncrypted = typing.Annotated[
    typing.Union[
        types.SecureCredentialsEncrypted
    ],
    pydantic.Field(discriminator='QUALNAME')
]
