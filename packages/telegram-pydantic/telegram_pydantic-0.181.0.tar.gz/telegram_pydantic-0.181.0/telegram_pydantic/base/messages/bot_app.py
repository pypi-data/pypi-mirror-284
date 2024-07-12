from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.BotApp - Layer 181
BotApp = typing.Annotated[
    typing.Union[
        types.messages.BotApp
    ],
    pydantic.Field(discriminator='QUALNAME')
]
