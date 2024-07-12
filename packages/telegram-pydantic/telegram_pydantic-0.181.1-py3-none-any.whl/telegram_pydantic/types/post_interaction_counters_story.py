from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PostInteractionCountersStory(BaseModel):
    """
    types.PostInteractionCountersStory
    ID: 0x8a480e27
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PostInteractionCountersStory'] = pydantic.Field(
        'types.PostInteractionCountersStory',
        alias='_'
    )

    story_id: int
    views: int
    forwards: int
    reactions: int
