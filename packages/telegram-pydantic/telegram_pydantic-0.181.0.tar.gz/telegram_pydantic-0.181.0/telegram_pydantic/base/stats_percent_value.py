from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StatsPercentValue - Layer 181
StatsPercentValue = typing.Annotated[
    typing.Union[
        types.StatsPercentValue
    ],
    pydantic.Field(discriminator='QUALNAME')
]
