from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StatsGroupTopAdmin - Layer 181
StatsGroupTopAdmin = typing.Annotated[
    typing.Union[
        types.StatsGroupTopAdmin
    ],
    pydantic.Field(discriminator='QUALNAME')
]
