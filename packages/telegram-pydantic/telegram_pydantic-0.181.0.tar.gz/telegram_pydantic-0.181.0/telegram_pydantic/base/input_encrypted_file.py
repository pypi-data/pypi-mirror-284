from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputEncryptedFile - Layer 181
InputEncryptedFile = typing.Annotated[
    typing.Union[
        types.InputEncryptedFile,
        types.InputEncryptedFileBigUploaded,
        types.InputEncryptedFileEmpty,
        types.InputEncryptedFileUploaded
    ],
    pydantic.Field(discriminator='QUALNAME')
]
