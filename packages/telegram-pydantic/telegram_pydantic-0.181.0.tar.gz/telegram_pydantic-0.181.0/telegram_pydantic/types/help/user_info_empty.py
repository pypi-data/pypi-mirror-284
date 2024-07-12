from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserInfoEmpty(BaseModel):
    """
    types.help.UserInfoEmpty
    ID: 0xf3ae2eed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.UserInfoEmpty'] = pydantic.Field(
        'types.help.UserInfoEmpty',
        alias='_'
    )

