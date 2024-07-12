from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotMessageReaction(BaseModel):
    """
    types.UpdateBotMessageReaction
    ID: 0xac21d3ce
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotMessageReaction'] = pydantic.Field(
        'types.UpdateBotMessageReaction',
        alias='_'
    )

    peer: "base.Peer"
    msg_id: int
    date: int
    actor: "base.Peer"
    old_reactions: list["base.Reaction"]
    new_reactions: list["base.Reaction"]
    qts: int
