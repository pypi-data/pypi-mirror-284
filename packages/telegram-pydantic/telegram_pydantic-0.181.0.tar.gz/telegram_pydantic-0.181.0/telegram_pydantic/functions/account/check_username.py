from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckUsername(BaseModel):
    """
    functions.account.CheckUsername
    ID: 0x2714d86c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.CheckUsername'] = pydantic.Field(
        'functions.account.CheckUsername',
        alias='_'
    )

    username: str
