from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class VerifyEmail(BaseModel):
    """
    functions.account.VerifyEmail
    ID: 0x32da4cf
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.VerifyEmail'] = pydantic.Field(
        'functions.account.VerifyEmail',
        alias='_'
    )

    purpose: "base.EmailVerifyPurpose"
    verification: "base.EmailVerification"
