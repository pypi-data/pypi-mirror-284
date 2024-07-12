from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewStoryReaction(BaseModel):
    """
    types.UpdateNewStoryReaction
    ID: 0x1824e40b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewStoryReaction'] = pydantic.Field(
        'types.UpdateNewStoryReaction',
        alias='_'
    )

    story_id: int
    peer: "base.Peer"
    reaction: "base.Reaction"
