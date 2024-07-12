from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessagePeerVote(BaseModel):
    """
    types.MessagePeerVote
    ID: 0xb6cc2d5c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessagePeerVote'] = pydantic.Field(
        'types.MessagePeerVote',
        alias='_'
    )

    peer: "base.Peer"
    option: bytes
    date: int
