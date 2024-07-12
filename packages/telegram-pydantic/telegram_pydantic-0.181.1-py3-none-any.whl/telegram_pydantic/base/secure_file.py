from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecureFile - Layer 181
SecureFile = typing.Annotated[
    typing.Union[
        types.SecureFile,
        types.SecureFileEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
