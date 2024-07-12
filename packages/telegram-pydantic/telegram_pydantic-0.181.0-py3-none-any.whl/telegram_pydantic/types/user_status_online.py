from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserStatusOnline(BaseModel):
    """
    types.UserStatusOnline
    ID: 0xedb93949
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserStatusOnline'] = pydantic.Field(
        'types.UserStatusOnline',
        alias='_'
    )

    expires: int
