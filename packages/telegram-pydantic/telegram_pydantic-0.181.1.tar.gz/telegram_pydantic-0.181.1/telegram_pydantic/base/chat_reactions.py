from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatReactions - Layer 181
ChatReactions = typing.Annotated[
    typing.Union[
        types.ChatReactionsAll,
        types.ChatReactionsNone,
        types.ChatReactionsSome
    ],
    pydantic.Field(discriminator='QUALNAME')
]
