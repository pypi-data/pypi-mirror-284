from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePeerLocated(BaseModel):
    """
    types.UpdatePeerLocated
    ID: 0xb4afcfb0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePeerLocated'] = pydantic.Field(
        'types.UpdatePeerLocated',
        alias='_'
    )

    peers: list["base.PeerLocated"]
