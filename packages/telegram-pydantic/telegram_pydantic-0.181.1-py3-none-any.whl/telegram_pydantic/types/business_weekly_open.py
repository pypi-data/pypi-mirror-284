from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessWeeklyOpen(BaseModel):
    """
    types.BusinessWeeklyOpen
    ID: 0x120b1ab9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessWeeklyOpen'] = pydantic.Field(
        'types.BusinessWeeklyOpen',
        alias='_'
    )

    start_minute: int
    end_minute: int
