from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantJoinByInvite(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantJoinByInvite
    ID: 0xfe9fc158
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantJoinByInvite'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantJoinByInvite',
        alias='_'
    )

    invite: "base.ExportedChatInvite"
    via_chatlist: typing.Optional[bool] = None
