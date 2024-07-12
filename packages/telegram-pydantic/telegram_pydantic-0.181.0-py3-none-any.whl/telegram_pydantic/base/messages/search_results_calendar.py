from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.SearchResultsCalendar - Layer 181
SearchResultsCalendar = typing.Annotated[
    typing.Union[
        types.messages.SearchResultsCalendar
    ],
    pydantic.Field(discriminator='QUALNAME')
]
