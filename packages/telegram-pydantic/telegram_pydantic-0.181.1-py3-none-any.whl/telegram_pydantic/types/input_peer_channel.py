from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerChannel(BaseModel):
    """
    types.InputPeerChannel
    ID: 0x27bcbbfc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerChannel'] = pydantic.Field(
        'types.InputPeerChannel',
        alias='_'
    )

    channel_id: int
    access_hash: int
