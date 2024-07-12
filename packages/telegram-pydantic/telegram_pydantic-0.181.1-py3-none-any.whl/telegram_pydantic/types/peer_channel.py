from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerChannel(BaseModel):
    """
    types.PeerChannel
    ID: 0xa2a5371e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerChannel'] = pydantic.Field(
        'types.PeerChannel',
        alias='_'
    )

    channel_id: int
