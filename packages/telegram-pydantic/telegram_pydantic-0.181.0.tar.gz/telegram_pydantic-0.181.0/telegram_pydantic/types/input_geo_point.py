from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputGeoPoint(BaseModel):
    """
    types.InputGeoPoint
    ID: 0x48222faf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputGeoPoint'] = pydantic.Field(
        'types.InputGeoPoint',
        alias='_'
    )

    lat: float
    long: float
    accuracy_radius: typing.Optional[int] = None
