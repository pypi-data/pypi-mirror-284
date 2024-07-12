from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StoryReaction - Layer 181
StoryReaction = typing.Annotated[
    typing.Union[
        types.StoryReaction,
        types.StoryReactionPublicForward,
        types.StoryReactionPublicRepost
    ],
    pydantic.Field(discriminator='QUALNAME')
]
