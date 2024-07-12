from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserInfo(BaseModel):
    """
    types.help.UserInfo
    ID: 0x1eb3758
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.UserInfo'] = pydantic.Field(
        'types.help.UserInfo',
        alias='_'
    )

    message: str
    entities: list["base.MessageEntity"]
    author: str
    date: int
