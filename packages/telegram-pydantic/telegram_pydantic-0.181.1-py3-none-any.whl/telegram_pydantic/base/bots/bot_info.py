from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# bots.BotInfo - Layer 181
BotInfo = typing.Annotated[
    typing.Union[
        types.bots.BotInfo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
