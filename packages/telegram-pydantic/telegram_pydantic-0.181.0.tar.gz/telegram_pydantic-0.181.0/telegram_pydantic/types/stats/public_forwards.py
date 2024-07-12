from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PublicForwards(BaseModel):
    """
    types.stats.PublicForwards
    ID: 0x93037e20
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.PublicForwards'] = pydantic.Field(
        'types.stats.PublicForwards',
        alias='_'
    )

    count: int
    forwards: list["base.PublicForward"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
