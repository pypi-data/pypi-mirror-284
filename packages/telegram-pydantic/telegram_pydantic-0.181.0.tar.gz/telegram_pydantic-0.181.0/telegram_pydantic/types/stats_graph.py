from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsGraph(BaseModel):
    """
    types.StatsGraph
    ID: 0x8ea464b6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsGraph'] = pydantic.Field(
        'types.StatsGraph',
        alias='_'
    )

    json_: "base.DataJSON" = pydantic.Field(..., alias='json')
    zoom_token: typing.Optional[str] = None
