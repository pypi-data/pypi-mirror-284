from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditLocation(BaseModel):
    """
    functions.channels.EditLocation
    ID: 0x58e63f6d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditLocation'] = pydantic.Field(
        'functions.channels.EditLocation',
        alias='_'
    )

    channel: "base.InputChannel"
    geo_point: "base.InputGeoPoint"
    address: str
