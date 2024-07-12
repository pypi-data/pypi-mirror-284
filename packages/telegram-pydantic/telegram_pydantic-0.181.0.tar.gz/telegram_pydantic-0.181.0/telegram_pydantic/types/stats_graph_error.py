from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsGraphError(BaseModel):
    """
    types.StatsGraphError
    ID: 0xbedc9822
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsGraphError'] = pydantic.Field(
        'types.StatsGraphError',
        alias='_'
    )

    error: str
