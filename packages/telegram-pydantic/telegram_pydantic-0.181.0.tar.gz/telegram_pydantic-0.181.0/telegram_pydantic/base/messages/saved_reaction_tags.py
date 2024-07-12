from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.SavedReactionTags - Layer 181
SavedReactionTags = typing.Annotated[
    typing.Union[
        types.messages.SavedReactionTags,
        types.messages.SavedReactionTagsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
