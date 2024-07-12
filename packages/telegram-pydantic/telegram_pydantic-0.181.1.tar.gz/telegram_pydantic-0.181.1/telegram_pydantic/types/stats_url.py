from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsURL(BaseModel):
    """
    types.StatsURL
    ID: 0x47a971e0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsURL'] = pydantic.Field(
        'types.StatsURL',
        alias='_'
    )

    url: str
