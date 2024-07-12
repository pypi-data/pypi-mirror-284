from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAccountTTL(BaseModel):
    """
    functions.account.GetAccountTTL
    ID: 0x8fc711d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetAccountTTL'] = pydantic.Field(
        'functions.account.GetAccountTTL',
        alias='_'
    )

