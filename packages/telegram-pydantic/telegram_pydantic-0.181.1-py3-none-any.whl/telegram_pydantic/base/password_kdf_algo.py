from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PasswordKdfAlgo - Layer 181
PasswordKdfAlgo = typing.Annotated[
    typing.Union[
        types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow,
        types.PasswordKdfAlgoUnknown
    ],
    pydantic.Field(discriminator='QUALNAME')
]
