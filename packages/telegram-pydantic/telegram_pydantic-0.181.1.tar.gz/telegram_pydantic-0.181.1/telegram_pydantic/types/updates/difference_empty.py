from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DifferenceEmpty(BaseModel):
    """
    types.updates.DifferenceEmpty
    ID: 0x5d75a138
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.DifferenceEmpty'] = pydantic.Field(
        'types.updates.DifferenceEmpty',
        alias='_'
    )

    date: int
    seq: int
