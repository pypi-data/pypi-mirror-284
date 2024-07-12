from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageStats(BaseModel):
    """
    types.stats.MessageStats
    ID: 0x7fe91c14
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.MessageStats'] = pydantic.Field(
        'types.stats.MessageStats',
        alias='_'
    )

    views_graph: "base.StatsGraph"
    reactions_by_emotion_graph: "base.StatsGraph"
