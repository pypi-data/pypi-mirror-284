from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BotInlineResult - Layer 181
BotInlineResult = typing.Annotated[
    typing.Union[
        types.BotInlineMediaResult,
        types.BotInlineResult
    ],
    pydantic.Field(discriminator='QUALNAME')
]
