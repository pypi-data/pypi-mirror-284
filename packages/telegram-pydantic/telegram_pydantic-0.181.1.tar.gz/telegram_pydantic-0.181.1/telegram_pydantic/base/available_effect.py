from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AvailableEffect - Layer 181
AvailableEffect = typing.Annotated[
    typing.Union[
        types.AvailableEffect
    ],
    pydantic.Field(discriminator='QUALNAME')
]
