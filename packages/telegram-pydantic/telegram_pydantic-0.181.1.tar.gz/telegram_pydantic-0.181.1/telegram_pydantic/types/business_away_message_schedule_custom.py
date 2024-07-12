from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessAwayMessageScheduleCustom(BaseModel):
    """
    types.BusinessAwayMessageScheduleCustom
    ID: 0xcc4d9ecc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessAwayMessageScheduleCustom'] = pydantic.Field(
        'types.BusinessAwayMessageScheduleCustom',
        alias='_'
    )

    start_date: int
    end_date: int
