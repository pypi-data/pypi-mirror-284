from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StatsGroupTopPoster - Layer 181
StatsGroupTopPoster = typing.Annotated[
    typing.Union[
        types.StatsGroupTopPoster
    ],
    pydantic.Field(discriminator='QUALNAME')
]
