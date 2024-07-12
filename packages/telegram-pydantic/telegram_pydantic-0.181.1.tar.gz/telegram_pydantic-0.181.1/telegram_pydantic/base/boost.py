from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Boost - Layer 181
Boost = typing.Annotated[
    typing.Union[
        types.Boost
    ],
    pydantic.Field(discriminator='QUALNAME')
]
