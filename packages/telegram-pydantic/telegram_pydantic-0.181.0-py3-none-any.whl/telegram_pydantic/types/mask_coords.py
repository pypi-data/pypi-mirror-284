from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MaskCoords(BaseModel):
    """
    types.MaskCoords
    ID: 0xaed6dbb2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MaskCoords'] = pydantic.Field(
        'types.MaskCoords',
        alias='_'
    )

    n: int
    x: float
    y: float
    zoom: float
