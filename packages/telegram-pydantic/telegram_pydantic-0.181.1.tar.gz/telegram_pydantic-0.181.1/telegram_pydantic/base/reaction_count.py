from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ReactionCount - Layer 181
ReactionCount = typing.Annotated[
    typing.Union[
        types.ReactionCount
    ],
    pydantic.Field(discriminator='QUALNAME')
]
