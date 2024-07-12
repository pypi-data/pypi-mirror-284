from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantLeft(BaseModel):
    """
    types.ChannelParticipantLeft
    ID: 0x1b03f006
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantLeft'] = pydantic.Field(
        'types.ChannelParticipantLeft',
        alias='_'
    )

    peer: "base.Peer"
