from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SearchResultsCalendarPeriod - Layer 181
SearchResultsCalendarPeriod = typing.Annotated[
    typing.Union[
        types.SearchResultsCalendarPeriod
    ],
    pydantic.Field(discriminator='QUALNAME')
]
