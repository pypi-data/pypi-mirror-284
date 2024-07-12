from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFullUser(BaseModel):
    """
    functions.users.GetFullUser
    ID: 0xb60f5918
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.users.GetFullUser'] = pydantic.Field(
        'functions.users.GetFullUser',
        alias='_'
    )

    id: "base.InputUser"
