from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StatsAbsValueAndPrev - Layer 181
StatsAbsValueAndPrev = typing.Annotated[
    typing.Union[
        types.StatsAbsValueAndPrev
    ],
    pydantic.Field(discriminator='QUALNAME')
]
