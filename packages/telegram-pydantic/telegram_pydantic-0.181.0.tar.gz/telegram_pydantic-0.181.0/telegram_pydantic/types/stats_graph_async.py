from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsGraphAsync(BaseModel):
    """
    types.StatsGraphAsync
    ID: 0x4a27eb2d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsGraphAsync'] = pydantic.Field(
        'types.StatsGraphAsync',
        alias='_'
    )

    token: str
