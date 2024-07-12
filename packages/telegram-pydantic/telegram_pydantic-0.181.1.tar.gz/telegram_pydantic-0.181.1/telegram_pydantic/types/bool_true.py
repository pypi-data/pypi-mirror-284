from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BoolTrue(BaseModel):
    """
    types.BoolTrue
    ID: 0x997275b5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BoolTrue'] = pydantic.Field(
        'types.BoolTrue',
        alias='_'
    )

