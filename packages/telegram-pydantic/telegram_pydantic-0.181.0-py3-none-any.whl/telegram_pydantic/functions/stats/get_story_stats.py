from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStoryStats(BaseModel):
    """
    functions.stats.GetStoryStats
    ID: 0x374fef40
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetStoryStats'] = pydantic.Field(
        'functions.stats.GetStoryStats',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    dark: typing.Optional[bool] = None
