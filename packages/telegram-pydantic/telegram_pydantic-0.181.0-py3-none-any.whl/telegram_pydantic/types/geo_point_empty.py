from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GeoPointEmpty(BaseModel):
    """
    types.GeoPointEmpty
    ID: 0x1117dd5f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GeoPointEmpty'] = pydantic.Field(
        'types.GeoPointEmpty',
        alias='_'
    )

