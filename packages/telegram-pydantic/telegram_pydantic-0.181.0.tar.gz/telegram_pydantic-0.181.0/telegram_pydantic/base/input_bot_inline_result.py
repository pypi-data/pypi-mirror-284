from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBotInlineResult - Layer 181
InputBotInlineResult = typing.Annotated[
    typing.Union[
        types.InputBotInlineResult,
        types.InputBotInlineResultDocument,
        types.InputBotInlineResultGame,
        types.InputBotInlineResultPhoto
    ],
    pydantic.Field(discriminator='QUALNAME')
]
