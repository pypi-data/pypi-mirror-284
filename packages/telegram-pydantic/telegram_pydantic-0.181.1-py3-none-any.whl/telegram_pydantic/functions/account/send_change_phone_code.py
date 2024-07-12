from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendChangePhoneCode(BaseModel):
    """
    functions.account.SendChangePhoneCode
    ID: 0x82574ae5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SendChangePhoneCode'] = pydantic.Field(
        'functions.account.SendChangePhoneCode',
        alias='_'
    )

    phone_number: str
    settings: "base.CodeSettings"
