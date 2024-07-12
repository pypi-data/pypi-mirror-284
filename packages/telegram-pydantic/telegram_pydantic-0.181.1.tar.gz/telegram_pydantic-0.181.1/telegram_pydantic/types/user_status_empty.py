from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserStatusEmpty(BaseModel):
    """
    types.UserStatusEmpty
    ID: 0x9d05049
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserStatusEmpty'] = pydantic.Field(
        'types.UserStatusEmpty',
        alias='_'
    )

