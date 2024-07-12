from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class VerifyPhone(BaseModel):
    """
    functions.account.VerifyPhone
    ID: 0x4dd3a7f6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.VerifyPhone'] = pydantic.Field(
        'functions.account.VerifyPhone',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
    phone_code: str
