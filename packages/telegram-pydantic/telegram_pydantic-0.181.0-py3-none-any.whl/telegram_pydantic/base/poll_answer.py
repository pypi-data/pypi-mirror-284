from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PollAnswer - Layer 181
PollAnswer = typing.Annotated[
    typing.Union[
        types.PollAnswer
    ],
    pydantic.Field(discriminator='QUALNAME')
]
