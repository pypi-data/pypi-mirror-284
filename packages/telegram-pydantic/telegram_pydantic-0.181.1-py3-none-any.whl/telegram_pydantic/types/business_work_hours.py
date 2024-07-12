from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessWorkHours(BaseModel):
    """
    types.BusinessWorkHours
    ID: 0x8c92b098
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessWorkHours'] = pydantic.Field(
        'types.BusinessWorkHours',
        alias='_'
    )

    timezone_id: str
    weekly_open: list["base.BusinessWeeklyOpen"]
    open_now: typing.Optional[bool] = None
