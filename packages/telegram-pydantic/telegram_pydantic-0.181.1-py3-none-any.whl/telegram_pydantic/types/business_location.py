from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessLocation(BaseModel):
    """
    types.BusinessLocation
    ID: 0xac5c1af7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessLocation'] = pydantic.Field(
        'types.BusinessLocation',
        alias='_'
    )

    address: str
    geo_point: typing.Optional["base.GeoPoint"] = None
