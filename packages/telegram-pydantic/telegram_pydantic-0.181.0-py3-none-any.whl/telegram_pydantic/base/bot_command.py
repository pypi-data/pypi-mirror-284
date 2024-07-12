from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BotCommand - Layer 181
BotCommand = typing.Annotated[
    typing.Union[
        types.BotCommand
    ],
    pydantic.Field(discriminator='QUALNAME')
]
