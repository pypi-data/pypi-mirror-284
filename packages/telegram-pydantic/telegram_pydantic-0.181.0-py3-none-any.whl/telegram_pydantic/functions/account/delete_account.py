from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteAccount(BaseModel):
    """
    functions.account.DeleteAccount
    ID: 0xa2c0cf74
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.DeleteAccount'] = pydantic.Field(
        'functions.account.DeleteAccount',
        alias='_'
    )

    reason: str
    password: typing.Optional["base.InputCheckPasswordSRP"] = None
