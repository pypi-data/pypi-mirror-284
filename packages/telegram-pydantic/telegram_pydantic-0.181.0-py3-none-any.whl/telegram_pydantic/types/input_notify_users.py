from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputNotifyUsers(BaseModel):
    """
    types.InputNotifyUsers
    ID: 0x193b4417
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputNotifyUsers'] = pydantic.Field(
        'types.InputNotifyUsers',
        alias='_'
    )

