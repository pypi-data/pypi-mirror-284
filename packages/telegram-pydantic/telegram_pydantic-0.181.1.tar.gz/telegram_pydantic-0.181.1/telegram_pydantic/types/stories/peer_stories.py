from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerStories(BaseModel):
    """
    types.stories.PeerStories
    ID: 0xcae68768
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.PeerStories'] = pydantic.Field(
        'types.stories.PeerStories',
        alias='_'
    )

    stories: "base.PeerStories"
    chats: list["base.Chat"]
    users: list["base.User"]
