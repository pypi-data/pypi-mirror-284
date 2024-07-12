from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchPosts(BaseModel):
    """
    functions.channels.SearchPosts
    ID: 0xd19f987b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.SearchPosts'] = pydantic.Field(
        'functions.channels.SearchPosts',
        alias='_'
    )

    hashtag: str
    offset_rate: int
    offset_peer: "base.InputPeer"
    offset_id: int
    limit: int
