from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonRequestPeer(BaseModel):
    """
    types.KeyboardButtonRequestPeer
    ID: 0x53d7bfd8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonRequestPeer'] = pydantic.Field(
        'types.KeyboardButtonRequestPeer',
        alias='_'
    )

    text: str
    button_id: int
    peer_type: "base.RequestPeerType"
    max_quantity: int
