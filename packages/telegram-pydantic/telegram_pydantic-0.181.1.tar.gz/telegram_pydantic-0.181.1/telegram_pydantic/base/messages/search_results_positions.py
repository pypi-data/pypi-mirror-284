from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.SearchResultsPositions - Layer 181
SearchResultsPositions = typing.Annotated[
    typing.Union[
        types.messages.SearchResultsPositions
    ],
    pydantic.Field(discriminator='QUALNAME')
]
