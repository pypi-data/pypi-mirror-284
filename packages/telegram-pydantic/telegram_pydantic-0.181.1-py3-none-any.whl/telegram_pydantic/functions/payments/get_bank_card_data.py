from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBankCardData(BaseModel):
    """
    functions.payments.GetBankCardData
    ID: 0x2e79d779
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetBankCardData'] = pydantic.Field(
        'functions.payments.GetBankCardData',
        alias='_'
    )

    number: str
