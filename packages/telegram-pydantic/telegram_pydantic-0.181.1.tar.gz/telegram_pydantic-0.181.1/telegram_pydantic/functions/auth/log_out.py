from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LogOut(BaseModel):
    """
    functions.auth.LogOut
    ID: 0x3e72ba19
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.LogOut'] = pydantic.Field(
        'functions.auth.LogOut',
        alias='_'
    )

