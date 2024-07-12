from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonRequestGeoLocation(BaseModel):
    """
    types.KeyboardButtonRequestGeoLocation
    ID: 0xfc796b3f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonRequestGeoLocation'] = pydantic.Field(
        'types.KeyboardButtonRequestGeoLocation',
        alias='_'
    )

    text: str
