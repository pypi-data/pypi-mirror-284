from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBotInlineMessageID - Layer 181
InputBotInlineMessageID = typing.Annotated[
    typing.Union[
        types.InputBotInlineMessageID,
        types.InputBotInlineMessageID64
    ],
    pydantic.Field(discriminator='QUALNAME')
]
