from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BoolFalse(BaseModel):
    """
    types.BoolFalse
    ID: 0xbc799737
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BoolFalse'] = pydantic.Field(
        'types.BoolFalse',
        alias='_'
    )

