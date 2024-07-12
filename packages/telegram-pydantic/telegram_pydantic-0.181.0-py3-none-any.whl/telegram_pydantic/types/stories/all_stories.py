from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AllStories(BaseModel):
    """
    types.stories.AllStories
    ID: 0x6efc5e81
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.AllStories'] = pydantic.Field(
        'types.stories.AllStories',
        alias='_'
    )

    count: int
    state: str
    peer_stories: list["base.PeerStories"]
    chats: list["base.Chat"]
    users: list["base.User"]
    stealth_mode: "base.StoriesStealthMode"
    has_more: typing.Optional[bool] = None
