from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotifyPeer(BaseModel):
    """
    types.NotifyPeer
    ID: 0x9fd40bd8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotifyPeer'] = pydantic.Field(
        'types.NotifyPeer',
        alias='_'
    )

    peer: "base.Peer"
