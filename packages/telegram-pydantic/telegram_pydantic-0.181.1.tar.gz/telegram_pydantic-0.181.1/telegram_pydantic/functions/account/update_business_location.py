from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBusinessLocation(BaseModel):
    """
    functions.account.UpdateBusinessLocation
    ID: 0x9e6b131a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateBusinessLocation'] = pydantic.Field(
        'functions.account.UpdateBusinessLocation',
        alias='_'
    )

    geo_point: typing.Optional["base.InputGeoPoint"] = None
    address: typing.Optional[str] = None
