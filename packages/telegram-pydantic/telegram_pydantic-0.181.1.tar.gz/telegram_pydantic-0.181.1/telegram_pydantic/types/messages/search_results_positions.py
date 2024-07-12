from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchResultsPositions(BaseModel):
    """
    types.messages.SearchResultsPositions
    ID: 0x53b22baf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SearchResultsPositions'] = pydantic.Field(
        'types.messages.SearchResultsPositions',
        alias='_'
    )

    count: int
    positions: list["base.SearchResultsPosition"]
