from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Reaction - Layer 181
Reaction = typing.Annotated[
    typing.Union[
        types.ReactionCustomEmoji,
        types.ReactionEmoji,
        types.ReactionEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
