from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantBanned(BaseModel):
    """
    types.ChannelParticipantBanned
    ID: 0x6df8014e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantBanned'] = pydantic.Field(
        'types.ChannelParticipantBanned',
        alias='_'
    )

    peer: "base.Peer"
    kicked_by: int
    date: int
    banned_rights: "base.ChatBannedRights"
    left: typing.Optional[bool] = None
