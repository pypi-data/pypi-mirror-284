from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Timezone(BaseModel):
    """
    types.Timezone
    ID: 0xff9289f5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Timezone'] = pydantic.Field(
        'types.Timezone',
        alias='_'
    )

    id: str
    name: str
    utc_offset: int
