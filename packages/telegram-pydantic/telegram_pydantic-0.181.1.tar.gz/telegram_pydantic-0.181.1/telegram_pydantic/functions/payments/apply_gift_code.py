from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ApplyGiftCode(BaseModel):
    """
    functions.payments.ApplyGiftCode
    ID: 0xf6e26854
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.ApplyGiftCode'] = pydantic.Field(
        'functions.payments.ApplyGiftCode',
        alias='_'
    )

    slug: str
