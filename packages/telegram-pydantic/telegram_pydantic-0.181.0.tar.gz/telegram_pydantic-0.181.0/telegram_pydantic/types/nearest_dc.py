from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NearestDc(BaseModel):
    """
    types.NearestDc
    ID: 0x8e1a1775
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NearestDc'] = pydantic.Field(
        'types.NearestDc',
        alias='_'
    )

    country: str
    this_dc: int
    nearest_dc: int
