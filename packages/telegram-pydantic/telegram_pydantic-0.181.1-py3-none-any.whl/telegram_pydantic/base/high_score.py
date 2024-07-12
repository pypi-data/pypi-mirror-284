from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# HighScore - Layer 181
HighScore = typing.Annotated[
    typing.Union[
        types.HighScore
    ],
    pydantic.Field(discriminator='QUALNAME')
]
