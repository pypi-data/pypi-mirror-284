from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryViewsList(BaseModel):
    """
    types.stories.StoryViewsList
    ID: 0x59d78fc5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.StoryViewsList'] = pydantic.Field(
        'types.stories.StoryViewsList',
        alias='_'
    )

    count: int
    views_count: int
    forwards_count: int
    reactions_count: int
    views: list["base.StoryView"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
