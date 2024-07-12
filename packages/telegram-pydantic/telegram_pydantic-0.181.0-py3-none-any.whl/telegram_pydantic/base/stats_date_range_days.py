from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StatsDateRangeDays - Layer 181
StatsDateRangeDays = typing.Annotated[
    typing.Union[
        types.StatsDateRangeDays
    ],
    pydantic.Field(discriminator='QUALNAME')
]
