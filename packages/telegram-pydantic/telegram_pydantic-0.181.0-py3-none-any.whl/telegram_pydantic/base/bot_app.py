from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BotApp - Layer 181
BotApp = typing.Annotated[
    typing.Union[
        types.BotApp,
        types.BotAppNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
