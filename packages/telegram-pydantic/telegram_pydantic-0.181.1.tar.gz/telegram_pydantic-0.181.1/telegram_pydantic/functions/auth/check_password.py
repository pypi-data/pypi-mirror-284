from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckPassword(BaseModel):
    """
    functions.auth.CheckPassword
    ID: 0xd18b4d16
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.CheckPassword'] = pydantic.Field(
        'functions.auth.CheckPassword',
        alias='_'
    )

    password: "base.InputCheckPasswordSRP"
