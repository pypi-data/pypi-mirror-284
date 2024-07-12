from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stats.BroadcastStats - Layer 181
BroadcastStats = typing.Annotated[
    typing.Union[
        types.stats.BroadcastStats
    ],
    pydantic.Field(discriminator='QUALNAME')
]
