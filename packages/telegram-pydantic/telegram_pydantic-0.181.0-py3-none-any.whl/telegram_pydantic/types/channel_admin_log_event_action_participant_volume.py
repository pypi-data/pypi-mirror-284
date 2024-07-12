from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantVolume(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantVolume
    ID: 0x3e7f6847
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantVolume'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantVolume',
        alias='_'
    )

    participant: "base.GroupCallParticipant"
