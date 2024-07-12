from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantToggleBan(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantToggleBan
    ID: 0xe6d83d7e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantToggleBan'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantToggleBan',
        alias='_'
    )

    prev_participant: "base.ChannelParticipant"
    new_participant: "base.ChannelParticipant"
