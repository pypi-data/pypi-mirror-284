from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MediaAreaGeoPoint(BaseModel):
    """
    types.MediaAreaGeoPoint
    ID: 0xdf8b3b22
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MediaAreaGeoPoint'] = pydantic.Field(
        'types.MediaAreaGeoPoint',
        alias='_'
    )

    coordinates: "base.MediaAreaCoordinates"
    geo: "base.GeoPoint"
