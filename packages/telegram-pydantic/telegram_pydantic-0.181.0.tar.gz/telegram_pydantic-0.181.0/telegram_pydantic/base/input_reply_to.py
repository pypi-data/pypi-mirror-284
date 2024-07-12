from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputReplyTo - Layer 181
InputReplyTo = typing.Annotated[
    typing.Union[
        types.InputReplyToMessage,
        types.InputReplyToStory
    ],
    pydantic.Field(discriminator='QUALNAME')
]
