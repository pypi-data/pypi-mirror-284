from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMessageReactions(BaseModel):
    """
    types.UpdateMessageReactions
    ID: 0x5e1b3cb8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMessageReactions'] = pydantic.Field(
        'types.UpdateMessageReactions',
        alias='_'
    )

    peer: "base.Peer"
    msg_id: int
    reactions: "base.MessageReactions"
    top_msg_id: typing.Optional[int] = None
