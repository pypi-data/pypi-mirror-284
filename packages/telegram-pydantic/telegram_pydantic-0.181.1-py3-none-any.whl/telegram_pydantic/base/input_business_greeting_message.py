from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBusinessGreetingMessage - Layer 181
InputBusinessGreetingMessage = typing.Annotated[
    typing.Union[
        types.InputBusinessGreetingMessage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
