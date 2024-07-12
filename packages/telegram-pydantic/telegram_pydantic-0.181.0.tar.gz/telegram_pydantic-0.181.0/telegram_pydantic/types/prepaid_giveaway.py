from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrepaidGiveaway(BaseModel):
    """
    types.PrepaidGiveaway
    ID: 0xb2539d54
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrepaidGiveaway'] = pydantic.Field(
        'types.PrepaidGiveaway',
        alias='_'
    )

    id: int
    months: int
    quantity: int
    date: int
