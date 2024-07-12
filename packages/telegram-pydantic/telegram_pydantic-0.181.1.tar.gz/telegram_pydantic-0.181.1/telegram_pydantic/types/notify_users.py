from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotifyUsers(BaseModel):
    """
    types.NotifyUsers
    ID: 0xb4c83b4c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotifyUsers'] = pydantic.Field(
        'types.NotifyUsers',
        alias='_'
    )

