from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetTmpPassword(BaseModel):
    """
    functions.account.GetTmpPassword
    ID: 0x449e0b51
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetTmpPassword'] = pydantic.Field(
        'functions.account.GetTmpPassword',
        alias='_'
    )

    password: "base.InputCheckPasswordSRP"
    period: int
