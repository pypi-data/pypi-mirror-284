from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantInvite(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantInvite
    ID: 0xe31c34d8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantInvite'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantInvite',
        alias='_'
    )

    participant: "base.ChannelParticipant"
