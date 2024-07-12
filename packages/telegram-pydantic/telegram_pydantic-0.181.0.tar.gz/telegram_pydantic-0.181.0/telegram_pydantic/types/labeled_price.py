from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LabeledPrice(BaseModel):
    """
    types.LabeledPrice
    ID: 0xcb296bf8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.LabeledPrice'] = pydantic.Field(
        'types.LabeledPrice',
        alias='_'
    )

    label: str
    amount: int
