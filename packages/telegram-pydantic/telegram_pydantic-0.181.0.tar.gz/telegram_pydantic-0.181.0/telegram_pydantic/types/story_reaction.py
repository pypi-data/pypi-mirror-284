from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryReaction(BaseModel):
    """
    types.StoryReaction
    ID: 0x6090d6d5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryReaction'] = pydantic.Field(
        'types.StoryReaction',
        alias='_'
    )

    peer_id: "base.Peer"
    date: int
    reaction: "base.Reaction"
