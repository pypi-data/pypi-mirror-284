from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSentStoryReaction(BaseModel):
    """
    types.UpdateSentStoryReaction
    ID: 0x7d627683
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSentStoryReaction'] = pydantic.Field(
        'types.UpdateSentStoryReaction',
        alias='_'
    )

    peer: "base.Peer"
    story_id: int
    reaction: "base.Reaction"
