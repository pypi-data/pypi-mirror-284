from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageReactions(BaseModel):
    """
    types.MessageReactions
    ID: 0x4f2b9479
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageReactions'] = pydantic.Field(
        'types.MessageReactions',
        alias='_'
    )

    results: list["base.ReactionCount"]
    min: typing.Optional[bool] = None
    can_see_list: typing.Optional[bool] = None
    reactions_as_tags: typing.Optional[bool] = None
    recent_reactions: typing.Optional[list["base.MessagePeerReaction"]] = None
