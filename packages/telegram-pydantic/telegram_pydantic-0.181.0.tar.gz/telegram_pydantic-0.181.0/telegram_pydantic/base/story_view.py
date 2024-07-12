from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StoryView - Layer 181
StoryView = typing.Annotated[
    typing.Union[
        types.StoryView,
        types.StoryViewPublicForward,
        types.StoryViewPublicRepost
    ],
    pydantic.Field(discriminator='QUALNAME')
]
