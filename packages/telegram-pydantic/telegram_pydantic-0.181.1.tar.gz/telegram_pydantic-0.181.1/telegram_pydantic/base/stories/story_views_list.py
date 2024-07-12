from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stories.StoryViewsList - Layer 181
StoryViewsList = typing.Annotated[
    typing.Union[
        types.stories.StoryViewsList
    ],
    pydantic.Field(discriminator='QUALNAME')
]
