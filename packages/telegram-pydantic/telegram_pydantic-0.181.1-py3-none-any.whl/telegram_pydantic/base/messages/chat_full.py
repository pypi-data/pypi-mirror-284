from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.ChatFull - Layer 181
ChatFull = typing.Annotated[
    typing.Union[
        types.messages.ChatFull
    ],
    pydantic.Field(discriminator='QUALNAME')
]
