from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SavedReactionTag - Layer 181
SavedReactionTag = typing.Annotated[
    typing.Union[
        types.SavedReactionTag
    ],
    pydantic.Field(discriminator='QUALNAME')
]
