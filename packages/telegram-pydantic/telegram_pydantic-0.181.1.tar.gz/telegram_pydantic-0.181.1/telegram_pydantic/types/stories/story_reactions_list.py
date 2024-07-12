from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryReactionsList(BaseModel):
    """
    types.stories.StoryReactionsList
    ID: 0xaa5f789c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.StoryReactionsList'] = pydantic.Field(
        'types.stories.StoryReactionsList',
        alias='_'
    )

    count: int
    reactions: list["base.StoryReaction"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
