from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SearchResultsPosition - Layer 181
SearchResultsPosition = typing.Annotated[
    typing.Union[
        types.SearchResultPosition
    ],
    pydantic.Field(discriminator='QUALNAME')
]
