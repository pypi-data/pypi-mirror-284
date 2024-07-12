from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.Reactions - Layer 181
Reactions = typing.Annotated[
    typing.Union[
        types.messages.Reactions,
        types.messages.ReactionsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
