from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EncryptedFile - Layer 181
EncryptedFile = typing.Annotated[
    typing.Union[
        types.EncryptedFile,
        types.EncryptedFileEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
