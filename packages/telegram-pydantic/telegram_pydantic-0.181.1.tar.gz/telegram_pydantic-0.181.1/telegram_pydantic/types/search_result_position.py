from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchResultPosition(BaseModel):
    """
    types.SearchResultPosition
    ID: 0x7f648b67
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SearchResultPosition'] = pydantic.Field(
        'types.SearchResultPosition',
        alias='_'
    )

    msg_id: int
    date: int
    offset: int
