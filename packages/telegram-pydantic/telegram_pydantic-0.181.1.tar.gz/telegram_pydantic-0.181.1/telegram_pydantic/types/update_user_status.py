from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUserStatus(BaseModel):
    """
    types.UpdateUserStatus
    ID: 0xe5bdf8de
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateUserStatus'] = pydantic.Field(
        'types.UpdateUserStatus',
        alias='_'
    )

    user_id: int
    status: "base.UserStatus"
