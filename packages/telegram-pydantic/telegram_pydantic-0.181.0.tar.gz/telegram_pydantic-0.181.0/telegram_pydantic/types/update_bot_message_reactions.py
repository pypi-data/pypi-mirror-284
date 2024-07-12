from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotMessageReactions(BaseModel):
    """
    types.UpdateBotMessageReactions
    ID: 0x9cb7759
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotMessageReactions'] = pydantic.Field(
        'types.UpdateBotMessageReactions',
        alias='_'
    )

    peer: "base.Peer"
    msg_id: int
    date: int
    reactions: list["base.ReactionCount"]
    qts: int
