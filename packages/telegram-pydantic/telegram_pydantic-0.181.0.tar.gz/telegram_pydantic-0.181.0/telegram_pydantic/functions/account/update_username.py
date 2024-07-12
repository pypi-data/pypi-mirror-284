from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUsername(BaseModel):
    """
    functions.account.UpdateUsername
    ID: 0x3e0bdd7c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateUsername'] = pydantic.Field(
        'functions.account.UpdateUsername',
        alias='_'
    )

    username: str
