from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGeoProximityReached(BaseModel):
    """
    types.MessageActionGeoProximityReached
    ID: 0x98e0d697
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGeoProximityReached'] = pydantic.Field(
        'types.MessageActionGeoProximityReached',
        alias='_'
    )

    from_id: "base.Peer"
    to_id: "base.Peer"
    distance: int
