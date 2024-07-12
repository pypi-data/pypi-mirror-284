from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stats.StoryStats - Layer 181
StoryStats = typing.Annotated[
    typing.Union[
        types.stats.StoryStats
    ],
    pydantic.Field(discriminator='QUALNAME')
]
