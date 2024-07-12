from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Game - Layer 181
Game = typing.Annotated[
    typing.Union[
        types.Game
    ],
    pydantic.Field(discriminator='QUALNAME')
]
