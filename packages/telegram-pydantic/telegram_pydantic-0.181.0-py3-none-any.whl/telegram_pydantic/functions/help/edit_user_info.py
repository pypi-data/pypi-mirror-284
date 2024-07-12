from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditUserInfo(BaseModel):
    """
    functions.help.EditUserInfo
    ID: 0x66b91b70
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.EditUserInfo'] = pydantic.Field(
        'functions.help.EditUserInfo',
        alias='_'
    )

    user_id: "base.InputUser"
    message: str
    entities: list["base.MessageEntity"]
