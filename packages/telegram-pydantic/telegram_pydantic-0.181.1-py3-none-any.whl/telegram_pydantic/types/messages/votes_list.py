from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class VotesList(BaseModel):
    """
    types.messages.VotesList
    ID: 0x4899484e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.VotesList'] = pydantic.Field(
        'types.messages.VotesList',
        alias='_'
    )

    count: int
    votes: list["base.MessagePeerVote"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
