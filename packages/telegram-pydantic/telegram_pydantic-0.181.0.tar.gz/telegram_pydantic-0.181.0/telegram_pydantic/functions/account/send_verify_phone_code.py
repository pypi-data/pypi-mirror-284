from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendVerifyPhoneCode(BaseModel):
    """
    functions.account.SendVerifyPhoneCode
    ID: 0xa5a356f9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SendVerifyPhoneCode'] = pydantic.Field(
        'functions.account.SendVerifyPhoneCode',
        alias='_'
    )

    phone_number: str
    settings: "base.CodeSettings"
