from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantUnmute(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantUnmute
    ID: 0xe64429c0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantUnmute'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantUnmute',
        alias='_'
    )

    participant: "base.GroupCallParticipant"
