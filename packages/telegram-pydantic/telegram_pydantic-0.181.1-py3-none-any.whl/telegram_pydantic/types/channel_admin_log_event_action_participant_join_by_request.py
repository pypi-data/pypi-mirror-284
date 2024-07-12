from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantJoinByRequest(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantJoinByRequest
    ID: 0xafb6144a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantJoinByRequest'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantJoinByRequest',
        alias='_'
    )

    invite: "base.ExportedChatInvite"
    approved_by: int
