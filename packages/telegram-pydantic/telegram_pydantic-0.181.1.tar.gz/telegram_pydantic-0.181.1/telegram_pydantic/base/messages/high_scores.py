from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.HighScores - Layer 181
HighScores = typing.Annotated[
    typing.Union[
        types.messages.HighScores
    ],
    pydantic.Field(discriminator='QUALNAME')
]
