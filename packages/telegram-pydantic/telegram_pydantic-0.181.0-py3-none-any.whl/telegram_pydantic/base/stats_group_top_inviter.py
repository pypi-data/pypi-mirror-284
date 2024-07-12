from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StatsGroupTopInviter - Layer 181
StatsGroupTopInviter = typing.Annotated[
    typing.Union[
        types.StatsGroupTopInviter
    ],
    pydantic.Field(discriminator='QUALNAME')
]
