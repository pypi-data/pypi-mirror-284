from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stories.AllStories - Layer 181
AllStories = typing.Annotated[
    typing.Union[
        types.stories.AllStories,
        types.stories.AllStoriesNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
