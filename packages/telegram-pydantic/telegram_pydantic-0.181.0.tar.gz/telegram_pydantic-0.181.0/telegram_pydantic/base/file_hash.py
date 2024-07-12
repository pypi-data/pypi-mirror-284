from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# FileHash - Layer 181
FileHash = typing.Annotated[
    typing.Union[
        types.FileHash
    ],
    pydantic.Field(discriminator='QUALNAME')
]
