from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePeerSettings(BaseModel):
    """
    types.UpdatePeerSettings
    ID: 0x6a7e7366
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePeerSettings'] = pydantic.Field(
        'types.UpdatePeerSettings',
        alias='_'
    )

    peer: "base.Peer"
    settings: "base.PeerSettings"
