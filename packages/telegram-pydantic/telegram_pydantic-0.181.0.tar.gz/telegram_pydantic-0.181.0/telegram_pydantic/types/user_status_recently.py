from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserStatusRecently(BaseModel):
    """
    types.UserStatusRecently
    ID: 0x7b197dc8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserStatusRecently'] = pydantic.Field(
        'types.UserStatusRecently',
        alias='_'
    )

    by_me: typing.Optional[bool] = None
