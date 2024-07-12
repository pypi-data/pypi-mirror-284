from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaGeoPoint(BaseModel):
    """
    types.InputMediaGeoPoint
    ID: 0xf9c44144
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaGeoPoint'] = pydantic.Field(
        'types.InputMediaGeoPoint',
        alias='_'
    )

    geo_point: "base.InputGeoPoint"
