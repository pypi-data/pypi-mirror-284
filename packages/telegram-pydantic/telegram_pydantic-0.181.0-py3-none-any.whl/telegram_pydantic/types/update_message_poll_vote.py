from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMessagePollVote(BaseModel):
    """
    types.UpdateMessagePollVote
    ID: 0x24f40e77
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMessagePollVote'] = pydantic.Field(
        'types.UpdateMessagePollVote',
        alias='_'
    )

    poll_id: int
    peer: "base.Peer"
    options: list[bytes]
    qts: int
