from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionRequestedPeerSentMe(BaseModel):
    """
    types.MessageActionRequestedPeerSentMe
    ID: 0x93b31848
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionRequestedPeerSentMe'] = pydantic.Field(
        'types.MessageActionRequestedPeerSentMe',
        alias='_'
    )

    button_id: int
    peers: list["base.RequestedPeer"]
