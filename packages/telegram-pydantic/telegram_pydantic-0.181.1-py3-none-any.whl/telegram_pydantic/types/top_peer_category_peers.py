from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryPeers(BaseModel):
    """
    types.TopPeerCategoryPeers
    ID: 0xfb834291
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryPeers'] = pydantic.Field(
        'types.TopPeerCategoryPeers',
        alias='_'
    )

    category: "base.TopPeerCategory"
    count: int
    peers: list["base.TopPeer"]
