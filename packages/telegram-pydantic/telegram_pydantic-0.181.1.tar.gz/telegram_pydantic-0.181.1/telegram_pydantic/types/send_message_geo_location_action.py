from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageGeoLocationAction(BaseModel):
    """
    types.SendMessageGeoLocationAction
    ID: 0x176f8ba1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageGeoLocationAction'] = pydantic.Field(
        'types.SendMessageGeoLocationAction',
        alias='_'
    )

