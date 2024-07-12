from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PostInteractionCounters - Layer 181
PostInteractionCounters = typing.Annotated[
    typing.Union[
        types.PostInteractionCountersMessage,
        types.PostInteractionCountersStory
    ],
    pydantic.Field(discriminator='QUALNAME')
]
