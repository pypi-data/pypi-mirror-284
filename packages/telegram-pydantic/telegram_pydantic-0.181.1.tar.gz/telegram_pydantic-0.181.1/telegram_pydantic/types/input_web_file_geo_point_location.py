from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputWebFileGeoPointLocation(BaseModel):
    """
    types.InputWebFileGeoPointLocation
    ID: 0x9f2221c9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputWebFileGeoPointLocation'] = pydantic.Field(
        'types.InputWebFileGeoPointLocation',
        alias='_'
    )

    geo_point: "base.InputGeoPoint"
    access_hash: int
    w: int
    h: int
    zoom: int
    scale: int
