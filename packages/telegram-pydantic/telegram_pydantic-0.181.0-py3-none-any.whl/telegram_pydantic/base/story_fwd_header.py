from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StoryFwdHeader - Layer 181
StoryFwdHeader = typing.Annotated[
    typing.Union[
        types.StoryFwdHeader
    ],
    pydantic.Field(discriminator='QUALNAME')
]
