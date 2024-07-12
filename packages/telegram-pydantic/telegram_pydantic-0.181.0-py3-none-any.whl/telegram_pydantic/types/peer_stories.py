from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerStories(BaseModel):
    """
    types.PeerStories
    ID: 0x9a35e999
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerStories'] = pydantic.Field(
        'types.PeerStories',
        alias='_'
    )

    peer: "base.Peer"
    stories: list["base.StoryItem"]
    max_read_id: typing.Optional[int] = None
