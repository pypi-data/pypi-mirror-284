from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Timezone - Layer 181
Timezone = typing.Annotated[
    typing.Union[
        types.Timezone
    ],
    pydantic.Field(discriminator='QUALNAME')
]
