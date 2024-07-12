from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ConfirmPasswordEmail(BaseModel):
    """
    functions.account.ConfirmPasswordEmail
    ID: 0x8fdf1920
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ConfirmPasswordEmail'] = pydantic.Field(
        'functions.account.ConfirmPasswordEmail',
        alias='_'
    )

    code: str
