from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckRecoveryPassword(BaseModel):
    """
    functions.auth.CheckRecoveryPassword
    ID: 0xd36bf79
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.CheckRecoveryPassword'] = pydantic.Field(
        'functions.auth.CheckRecoveryPassword',
        alias='_'
    )

    code: str
