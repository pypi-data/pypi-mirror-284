from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BankCardData(BaseModel):
    """
    types.payments.BankCardData
    ID: 0x3e24e573
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.BankCardData'] = pydantic.Field(
        'types.payments.BankCardData',
        alias='_'
    )

    title: str
    open_urls: list["base.BankCardOpenUrl"]
