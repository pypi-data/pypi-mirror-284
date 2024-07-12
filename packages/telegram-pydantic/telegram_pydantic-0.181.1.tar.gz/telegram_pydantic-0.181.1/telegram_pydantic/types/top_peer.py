from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeer(BaseModel):
    """
    types.TopPeer
    ID: 0xedcdc05b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeer'] = pydantic.Field(
        'types.TopPeer',
        alias='_'
    )

    peer: "base.Peer"
    rating: float
