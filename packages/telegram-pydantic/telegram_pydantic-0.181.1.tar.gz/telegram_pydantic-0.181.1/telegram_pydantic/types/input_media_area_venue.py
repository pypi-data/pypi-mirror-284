from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaAreaVenue(BaseModel):
    """
    types.InputMediaAreaVenue
    ID: 0xb282217f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaAreaVenue'] = pydantic.Field(
        'types.InputMediaAreaVenue',
        alias='_'
    )

    coordinates: "base.MediaAreaCoordinates"
    query_id: int
    result_id: str
