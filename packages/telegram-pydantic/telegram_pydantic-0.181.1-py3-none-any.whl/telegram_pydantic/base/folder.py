from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Folder - Layer 181
Folder = typing.Annotated[
    typing.Union[
        types.Folder
    ],
    pydantic.Field(discriminator='QUALNAME')
]
