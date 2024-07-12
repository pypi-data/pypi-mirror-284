from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaGeoLive(BaseModel):
    """
    types.MessageMediaGeoLive
    ID: 0xb940c666
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaGeoLive'] = pydantic.Field(
        'types.MessageMediaGeoLive',
        alias='_'
    )

    geo: "base.GeoPoint"
    period: int
    heading: typing.Optional[int] = None
    proximity_notification_radius: typing.Optional[int] = None
