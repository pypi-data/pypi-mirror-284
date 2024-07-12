from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsGroupTopAdmin(BaseModel):
    """
    types.StatsGroupTopAdmin
    ID: 0xd7584c87
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsGroupTopAdmin'] = pydantic.Field(
        'types.StatsGroupTopAdmin',
        alias='_'
    )

    user_id: int
    deleted: int
    kicked: int
    banned: int
