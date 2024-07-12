from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecurePasswordKdfAlgo - Layer 181
SecurePasswordKdfAlgo = typing.Annotated[
    typing.Union[
        types.SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000,
        types.SecurePasswordKdfAlgoSHA512,
        types.SecurePasswordKdfAlgoUnknown
    ],
    pydantic.Field(discriminator='QUALNAME')
]
