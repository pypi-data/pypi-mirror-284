from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageReactions - Layer 181
MessageReactions = typing.Annotated[
    typing.Union[
        types.MessageReactions
    ],
    pydantic.Field(discriminator='QUALNAME')
]
