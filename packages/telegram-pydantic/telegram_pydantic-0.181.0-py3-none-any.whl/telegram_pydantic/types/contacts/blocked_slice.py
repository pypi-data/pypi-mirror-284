from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BlockedSlice(BaseModel):
    """
    types.contacts.BlockedSlice
    ID: 0xe1664194
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.BlockedSlice'] = pydantic.Field(
        'types.contacts.BlockedSlice',
        alias='_'
    )

    count: int
    blocked: list["base.PeerBlocked"]
    chats: list["base.Chat"]
    users: list["base.User"]
