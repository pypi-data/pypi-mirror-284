from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessagePeerVoteMultiple(BaseModel):
    """
    types.MessagePeerVoteMultiple
    ID: 0x4628f6e6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessagePeerVoteMultiple'] = pydantic.Field(
        'types.MessagePeerVoteMultiple',
        alias='_'
    )

    peer: "base.Peer"
    options: list[bytes]
    date: int
