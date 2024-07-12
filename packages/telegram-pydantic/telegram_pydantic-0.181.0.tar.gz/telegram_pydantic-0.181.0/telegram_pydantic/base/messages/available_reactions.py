from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.AvailableReactions - Layer 181
AvailableReactions = typing.Annotated[
    typing.Union[
        types.messages.AvailableReactions,
        types.messages.AvailableReactionsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
