from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stories.PeerStories - Layer 181
PeerStories = typing.Annotated[
    typing.Union[
        types.stories.PeerStories
    ],
    pydantic.Field(discriminator='QUALNAME')
]
