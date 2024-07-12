from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerBlocked(BaseModel):
    """
    types.PeerBlocked
    ID: 0xe8fd8014
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerBlocked'] = pydantic.Field(
        'types.PeerBlocked',
        alias='_'
    )

    peer_id: "base.Peer"
    date: int
