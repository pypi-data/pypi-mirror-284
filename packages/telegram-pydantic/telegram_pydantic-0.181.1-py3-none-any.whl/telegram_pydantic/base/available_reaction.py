from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AvailableReaction - Layer 181
AvailableReaction = typing.Annotated[
    typing.Union[
        types.AvailableReaction
    ],
    pydantic.Field(discriminator='QUALNAME')
]
