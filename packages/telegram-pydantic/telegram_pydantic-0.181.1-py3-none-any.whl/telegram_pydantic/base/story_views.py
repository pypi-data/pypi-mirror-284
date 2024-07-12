from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StoryViews - Layer 181
StoryViews = typing.Annotated[
    typing.Union[
        types.StoryViews
    ],
    pydantic.Field(discriminator='QUALNAME')
]
