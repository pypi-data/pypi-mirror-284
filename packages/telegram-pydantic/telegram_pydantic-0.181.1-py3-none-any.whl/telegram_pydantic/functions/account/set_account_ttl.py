from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetAccountTTL(BaseModel):
    """
    functions.account.SetAccountTTL
    ID: 0x2442485e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetAccountTTL'] = pydantic.Field(
        'functions.account.SetAccountTTL',
        alias='_'
    )

    ttl: "base.AccountDaysTTL"
