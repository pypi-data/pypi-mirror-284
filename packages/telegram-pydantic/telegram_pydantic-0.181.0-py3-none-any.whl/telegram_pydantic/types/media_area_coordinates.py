from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MediaAreaCoordinates(BaseModel):
    """
    types.MediaAreaCoordinates
    ID: 0x3d1ea4e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MediaAreaCoordinates'] = pydantic.Field(
        'types.MediaAreaCoordinates',
        alias='_'
    )

    x: float
    y: float
    w: float
    h: float
    rotation: float
