from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CreateChannel(BaseModel):
    """
    functions.channels.CreateChannel
    ID: 0x91006707
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.CreateChannel'] = pydantic.Field(
        'functions.channels.CreateChannel',
        alias='_'
    )

    title: str
    about: str
    broadcast: typing.Optional[bool] = None
    megagroup: typing.Optional[bool] = None
    for_import: typing.Optional[bool] = None
    forum: typing.Optional[bool] = None
    geo_point: typing.Optional["base.InputGeoPoint"] = None
    address: typing.Optional[str] = None
    ttl_period: typing.Optional[int] = None
