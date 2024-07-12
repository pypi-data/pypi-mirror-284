from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserStatusLastWeek(BaseModel):
    """
    types.UserStatusLastWeek
    ID: 0x541a1d1a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserStatusLastWeek'] = pydantic.Field(
        'types.UserStatusLastWeek',
        alias='_'
    )

    by_me: typing.Optional[bool] = None
