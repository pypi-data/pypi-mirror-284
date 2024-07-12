from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerLocated(BaseModel):
    """
    types.PeerLocated
    ID: 0xca461b5d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerLocated'] = pydantic.Field(
        'types.PeerLocated',
        alias='_'
    )

    peer: "base.Peer"
    expires: int
    distance: int
