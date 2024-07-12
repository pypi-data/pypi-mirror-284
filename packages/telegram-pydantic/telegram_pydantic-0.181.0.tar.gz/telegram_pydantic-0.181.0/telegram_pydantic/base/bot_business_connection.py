from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BotBusinessConnection - Layer 181
BotBusinessConnection = typing.Annotated[
    typing.Union[
        types.BotBusinessConnection
    ],
    pydantic.Field(discriminator='QUALNAME')
]
