from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBusinessAwayMessage - Layer 181
InputBusinessAwayMessage = typing.Annotated[
    typing.Union[
        types.InputBusinessAwayMessage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
