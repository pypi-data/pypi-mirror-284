from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StoryItem - Layer 181
StoryItem = typing.Annotated[
    typing.Union[
        types.StoryItem,
        types.StoryItemDeleted,
        types.StoryItemSkipped
    ],
    pydantic.Field(discriminator='QUALNAME')
]
