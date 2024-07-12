from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserEmpty(BaseModel):
    """
    types.UserEmpty
    ID: 0xd3bc4b7a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserEmpty'] = pydantic.Field(
        'types.UserEmpty',
        alias='_'
    )

    id: int
