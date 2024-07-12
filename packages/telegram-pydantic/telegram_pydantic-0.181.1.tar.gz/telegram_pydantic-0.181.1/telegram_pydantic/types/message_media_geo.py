from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaGeo(BaseModel):
    """
    types.MessageMediaGeo
    ID: 0x56e0d474
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaGeo'] = pydantic.Field(
        'types.MessageMediaGeo',
        alias='_'
    )

    geo: "base.GeoPoint"
