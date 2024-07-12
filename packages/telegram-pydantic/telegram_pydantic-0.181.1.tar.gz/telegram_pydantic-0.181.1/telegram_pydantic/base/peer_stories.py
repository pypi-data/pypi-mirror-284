from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PeerStories - Layer 181
PeerStories = typing.Annotated[
    typing.Union[
        types.PeerStories
    ],
    pydantic.Field(discriminator='QUALNAME')
]
