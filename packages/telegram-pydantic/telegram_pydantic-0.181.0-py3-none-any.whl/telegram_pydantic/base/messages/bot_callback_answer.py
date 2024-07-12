from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.BotCallbackAnswer - Layer 181
BotCallbackAnswer = typing.Annotated[
    typing.Union[
        types.messages.BotCallbackAnswer
    ],
    pydantic.Field(discriminator='QUALNAME')
]
