from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryStats(BaseModel):
    """
    types.stats.StoryStats
    ID: 0x50cd067c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.StoryStats'] = pydantic.Field(
        'types.stats.StoryStats',
        alias='_'
    )

    views_graph: "base.StatsGraph"
    reactions_by_emotion_graph: "base.StatsGraph"
