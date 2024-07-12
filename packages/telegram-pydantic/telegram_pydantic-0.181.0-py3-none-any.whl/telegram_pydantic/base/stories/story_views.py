from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stories.StoryViews - Layer 181
StoryViews = typing.Annotated[
    typing.Union[
        types.stories.StoryViews
    ],
    pydantic.Field(discriminator='QUALNAME')
]
