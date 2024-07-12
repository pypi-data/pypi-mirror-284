from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PollResults - Layer 181
PollResults = typing.Annotated[
    typing.Union[
        types.PollResults
    ],
    pydantic.Field(discriminator='QUALNAME')
]
