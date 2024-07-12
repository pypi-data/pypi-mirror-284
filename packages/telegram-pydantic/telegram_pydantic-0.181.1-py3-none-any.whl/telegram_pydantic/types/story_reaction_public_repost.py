from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryReactionPublicRepost(BaseModel):
    """
    types.StoryReactionPublicRepost
    ID: 0xcfcd0f13
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryReactionPublicRepost'] = pydantic.Field(
        'types.StoryReactionPublicRepost',
        alias='_'
    )

    peer_id: "base.Peer"
    story: "base.StoryItem"
