from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantMute(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantMute
    ID: 0xf92424d2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantMute'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantMute',
        alias='_'
    )

    participant: "base.GroupCallParticipant"
