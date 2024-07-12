from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantToggleAdmin(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantToggleAdmin
    ID: 0xd5676710
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantToggleAdmin'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantToggleAdmin',
        alias='_'
    )

    prev_participant: "base.ChannelParticipant"
    new_participant: "base.ChannelParticipant"
