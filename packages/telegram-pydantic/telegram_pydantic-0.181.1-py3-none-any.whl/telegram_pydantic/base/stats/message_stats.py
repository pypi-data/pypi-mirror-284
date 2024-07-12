from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stats.MessageStats - Layer 181
MessageStats = typing.Annotated[
    typing.Union[
        types.stats.MessageStats
    ],
    pydantic.Field(discriminator='QUALNAME')
]
