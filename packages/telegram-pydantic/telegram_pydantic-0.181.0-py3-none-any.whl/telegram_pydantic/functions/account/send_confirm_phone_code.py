from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendConfirmPhoneCode(BaseModel):
    """
    functions.account.SendConfirmPhoneCode
    ID: 0x1b3faa88
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SendConfirmPhoneCode'] = pydantic.Field(
        'functions.account.SendConfirmPhoneCode',
        alias='_'
    )

    hash: str
    settings: "base.CodeSettings"
