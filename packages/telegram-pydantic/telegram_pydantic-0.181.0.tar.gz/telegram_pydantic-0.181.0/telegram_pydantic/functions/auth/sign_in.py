from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SignIn(BaseModel):
    """
    functions.auth.SignIn
    ID: 0x8d52a951
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.SignIn'] = pydantic.Field(
        'functions.auth.SignIn',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
    phone_code: typing.Optional[str] = None
    email_verification: typing.Optional["base.EmailVerification"] = None
