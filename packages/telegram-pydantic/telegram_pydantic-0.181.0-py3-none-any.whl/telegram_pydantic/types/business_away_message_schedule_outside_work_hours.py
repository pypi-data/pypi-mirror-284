from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessAwayMessageScheduleOutsideWorkHours(BaseModel):
    """
    types.BusinessAwayMessageScheduleOutsideWorkHours
    ID: 0xc3f2f501
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessAwayMessageScheduleOutsideWorkHours'] = pydantic.Field(
        'types.BusinessAwayMessageScheduleOutsideWorkHours',
        alias='_'
    )

