from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AccountDaysTTL(BaseModel):
    """
    types.AccountDaysTTL
    ID: 0xb8d0afdf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AccountDaysTTL'] = pydantic.Field(
        'types.AccountDaysTTL',
        alias='_'
    )

    days: int
