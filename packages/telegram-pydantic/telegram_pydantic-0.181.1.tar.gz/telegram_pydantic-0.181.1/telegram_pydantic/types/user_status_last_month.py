from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserStatusLastMonth(BaseModel):
    """
    types.UserStatusLastMonth
    ID: 0x65899777
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserStatusLastMonth'] = pydantic.Field(
        'types.UserStatusLastMonth',
        alias='_'
    )

    by_me: typing.Optional[bool] = None
