from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DataJSON(BaseModel):
    """
    types.DataJSON
    ID: 0x7d748d04
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DataJSON'] = pydantic.Field(
        'types.DataJSON',
        alias='_'
    )

    data: str
