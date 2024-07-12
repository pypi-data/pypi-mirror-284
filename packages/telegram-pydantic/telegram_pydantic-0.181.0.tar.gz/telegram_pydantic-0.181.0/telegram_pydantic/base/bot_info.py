from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BotInfo - Layer 181
BotInfo = typing.Annotated[
    typing.Union[
        types.BotInfo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
