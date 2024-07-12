from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBroadcastStats(BaseModel):
    """
    functions.stats.GetBroadcastStats
    ID: 0xab42441a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetBroadcastStats'] = pydantic.Field(
        'functions.stats.GetBroadcastStats',
        alias='_'
    )

    channel: "base.InputChannel"
    dark: typing.Optional[bool] = None
