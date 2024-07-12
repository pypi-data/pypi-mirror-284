from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChangePhone(BaseModel):
    """
    functions.account.ChangePhone
    ID: 0x70c32edb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ChangePhone'] = pydantic.Field(
        'functions.account.ChangePhone',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
    phone_code: str
