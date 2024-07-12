from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetLoginEmail(BaseModel):
    """
    functions.auth.ResetLoginEmail
    ID: 0x7e960193
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ResetLoginEmail'] = pydantic.Field(
        'functions.auth.ResetLoginEmail',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
