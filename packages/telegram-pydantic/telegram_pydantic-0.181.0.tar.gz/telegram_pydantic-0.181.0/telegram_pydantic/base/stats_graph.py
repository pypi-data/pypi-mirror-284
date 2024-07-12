from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StatsGraph - Layer 181
StatsGraph = typing.Annotated[
    typing.Union[
        types.StatsGraph,
        types.StatsGraphAsync,
        types.StatsGraphError
    ],
    pydantic.Field(discriminator='QUALNAME')
]
