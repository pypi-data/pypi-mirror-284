from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stories.StoryReactionsList - Layer 181
StoryReactionsList = typing.Annotated[
    typing.Union[
        types.stories.StoryReactionsList
    ],
    pydantic.Field(discriminator='QUALNAME')
]
