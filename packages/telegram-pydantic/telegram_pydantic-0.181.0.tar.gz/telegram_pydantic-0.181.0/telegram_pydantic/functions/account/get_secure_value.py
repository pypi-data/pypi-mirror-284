from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSecureValue(BaseModel):
    """
    functions.account.GetSecureValue
    ID: 0x73665bc2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetSecureValue'] = pydantic.Field(
        'functions.account.GetSecureValue',
        alias='_'
    )

    types: list["base.SecureValueType"]
