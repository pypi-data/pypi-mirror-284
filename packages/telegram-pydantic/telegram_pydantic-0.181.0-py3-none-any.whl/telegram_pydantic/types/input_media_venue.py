from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaVenue(BaseModel):
    """
    types.InputMediaVenue
    ID: 0xc13d1c11
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaVenue'] = pydantic.Field(
        'types.InputMediaVenue',
        alias='_'
    )

    geo_point: "base.InputGeoPoint"
    title: str
    address: str
    provider: str
    venue_id: str
    venue_type: str
