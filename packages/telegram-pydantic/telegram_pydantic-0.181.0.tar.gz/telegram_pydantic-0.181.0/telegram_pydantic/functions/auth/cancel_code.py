from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CancelCode(BaseModel):
    """
    functions.auth.CancelCode
    ID: 0x1f040578
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.CancelCode'] = pydantic.Field(
        'functions.auth.CancelCode',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
