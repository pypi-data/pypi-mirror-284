from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsDateRangeDays(BaseModel):
    """
    types.StatsDateRangeDays
    ID: 0xb637edaf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsDateRangeDays'] = pydantic.Field(
        'types.StatsDateRangeDays',
        alias='_'
    )

    min_date: int
    max_date: int
