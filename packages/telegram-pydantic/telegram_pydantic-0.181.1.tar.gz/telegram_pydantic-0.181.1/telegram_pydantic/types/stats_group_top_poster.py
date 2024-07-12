from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsGroupTopPoster(BaseModel):
    """
    types.StatsGroupTopPoster
    ID: 0x9d04af9b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsGroupTopPoster'] = pydantic.Field(
        'types.StatsGroupTopPoster',
        alias='_'
    )

    user_id: int
    messages: int
    avg_chars: int
