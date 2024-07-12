from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MegagroupStats(BaseModel):
    """
    types.stats.MegagroupStats
    ID: 0xef7ff916
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.MegagroupStats'] = pydantic.Field(
        'types.stats.MegagroupStats',
        alias='_'
    )

    period: "base.StatsDateRangeDays"
    members: "base.StatsAbsValueAndPrev"
    messages: "base.StatsAbsValueAndPrev"
    viewers: "base.StatsAbsValueAndPrev"
    posters: "base.StatsAbsValueAndPrev"
    growth_graph: "base.StatsGraph"
    members_graph: "base.StatsGraph"
    new_members_by_source_graph: "base.StatsGraph"
    languages_graph: "base.StatsGraph"
    messages_graph: "base.StatsGraph"
    actions_graph: "base.StatsGraph"
    top_hours_graph: "base.StatsGraph"
    weekdays_graph: "base.StatsGraph"
    top_posters: list["base.StatsGroupTopPoster"]
    top_admins: list["base.StatsGroupTopAdmin"]
    top_inviters: list["base.StatsGroupTopInviter"]
    users: list["base.User"]
