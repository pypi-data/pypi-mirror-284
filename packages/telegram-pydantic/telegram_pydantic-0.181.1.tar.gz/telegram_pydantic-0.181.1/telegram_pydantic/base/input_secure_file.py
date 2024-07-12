from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputSecureFile - Layer 181
InputSecureFile = typing.Annotated[
    typing.Union[
        types.InputSecureFile,
        types.InputSecureFileUploaded
    ],
    pydantic.Field(discriminator='QUALNAME')
]
