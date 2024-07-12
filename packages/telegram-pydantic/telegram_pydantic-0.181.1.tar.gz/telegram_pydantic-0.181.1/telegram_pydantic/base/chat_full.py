from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatFull - Layer 181
ChatFull = typing.Annotated[
    typing.Union[
        types.ChannelFull,
        types.ChatFull
    ],
    pydantic.Field(discriminator='QUALNAME')
]
