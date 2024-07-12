from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteSecureValue(BaseModel):
    """
    functions.account.DeleteSecureValue
    ID: 0xb880bc4b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.DeleteSecureValue'] = pydantic.Field(
        'functions.account.DeleteSecureValue',
        alias='_'
    )

    types: list["base.SecureValueType"]
