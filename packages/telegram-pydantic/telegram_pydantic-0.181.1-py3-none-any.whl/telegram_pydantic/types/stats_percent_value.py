from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsPercentValue(BaseModel):
    """
    types.StatsPercentValue
    ID: 0xcbce2fe0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsPercentValue'] = pydantic.Field(
        'types.StatsPercentValue',
        alias='_'
    )

    part: float
    total: float
