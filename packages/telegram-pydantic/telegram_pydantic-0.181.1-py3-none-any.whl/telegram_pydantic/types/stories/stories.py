from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Stories(BaseModel):
    """
    types.stories.Stories
    ID: 0x63c3dd0a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.Stories'] = pydantic.Field(
        'types.stories.Stories',
        alias='_'
    )

    count: int
    stories: list["base.StoryItem"]
    chats: list["base.Chat"]
    users: list["base.User"]
    pinned_to_top: typing.Optional[list[int]] = None
