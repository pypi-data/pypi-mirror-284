from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetPassword(BaseModel):
    """
    functions.account.ResetPassword
    ID: 0x9308ce1b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResetPassword'] = pydantic.Field(
        'functions.account.ResetPassword',
        alias='_'
    )

