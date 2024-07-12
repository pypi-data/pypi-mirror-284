from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Null - Layer 181
Null = typing.Annotated[
    typing.Union[
        types.Null
    ],
    pydantic.Field(discriminator='QUALNAME')
]
