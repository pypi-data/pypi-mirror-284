from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelLocation(BaseModel):
    """
    types.ChannelLocation
    ID: 0x209b82db
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelLocation'] = pydantic.Field(
        'types.ChannelLocation',
        alias='_'
    )

    geo_point: "base.GeoPoint"
    address: str
