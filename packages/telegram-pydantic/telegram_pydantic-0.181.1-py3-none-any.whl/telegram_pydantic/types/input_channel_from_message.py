from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChannelFromMessage(BaseModel):
    """
    types.InputChannelFromMessage
    ID: 0x5b934f9d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChannelFromMessage'] = pydantic.Field(
        'types.InputChannelFromMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    channel_id: int
