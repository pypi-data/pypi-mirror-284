from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPassword(BaseModel):
    """
    functions.account.GetPassword
    ID: 0x548a30f5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetPassword'] = pydantic.Field(
        'functions.account.GetPassword',
        alias='_'
    )

