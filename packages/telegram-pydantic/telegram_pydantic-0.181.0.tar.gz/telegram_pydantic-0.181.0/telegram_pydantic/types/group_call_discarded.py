from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCallDiscarded(BaseModel):
    """
    types.GroupCallDiscarded
    ID: 0x7780bcb4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GroupCallDiscarded'] = pydantic.Field(
        'types.GroupCallDiscarded',
        alias='_'
    )

    id: int
    access_hash: int
    duration: int
