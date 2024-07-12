from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PollAnswerVoters - Layer 181
PollAnswerVoters = typing.Annotated[
    typing.Union[
        types.PollAnswerVoters
    ],
    pydantic.Field(discriminator='QUALNAME')
]
