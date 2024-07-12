from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessAwayMessageScheduleAlways(BaseModel):
    """
    types.BusinessAwayMessageScheduleAlways
    ID: 0xc9b9e2b9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessAwayMessageScheduleAlways'] = pydantic.Field(
        'types.BusinessAwayMessageScheduleAlways',
        alias='_'
    )

