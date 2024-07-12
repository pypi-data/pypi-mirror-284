from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStarsBalance(BaseModel):
    """
    types.UpdateStarsBalance
    ID: 0xfb85198
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateStarsBalance'] = pydantic.Field(
        'types.UpdateStarsBalance',
        alias='_'
    )

    balance: int
