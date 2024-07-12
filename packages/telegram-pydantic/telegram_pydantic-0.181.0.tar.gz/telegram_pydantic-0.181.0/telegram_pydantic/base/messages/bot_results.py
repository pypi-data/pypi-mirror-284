from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.BotResults - Layer 181
BotResults = typing.Annotated[
    typing.Union[
        types.messages.BotResults
    ],
    pydantic.Field(discriminator='QUALNAME')
]
