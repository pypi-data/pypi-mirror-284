from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StatsURL - Layer 181
StatsURL = typing.Annotated[
    typing.Union[
        types.StatsURL
    ],
    pydantic.Field(discriminator='QUALNAME')
]
