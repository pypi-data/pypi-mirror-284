from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BotMenuButton - Layer 181
BotMenuButton = typing.Annotated[
    typing.Union[
        types.BotMenuButton,
        types.BotMenuButtonCommands,
        types.BotMenuButtonDefault
    ],
    pydantic.Field(discriminator='QUALNAME')
]
