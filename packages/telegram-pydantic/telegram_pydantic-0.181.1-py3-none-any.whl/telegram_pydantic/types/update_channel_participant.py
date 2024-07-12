from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelParticipant(BaseModel):
    """
    types.UpdateChannelParticipant
    ID: 0x985d3abb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelParticipant'] = pydantic.Field(
        'types.UpdateChannelParticipant',
        alias='_'
    )

    channel_id: int
    date: int
    actor_id: int
    user_id: int
    qts: int
    via_chatlist: typing.Optional[bool] = None
    prev_participant: typing.Optional["base.ChannelParticipant"] = None
    new_participant: typing.Optional["base.ChannelParticipant"] = None
    invite: typing.Optional["base.ExportedChatInvite"] = None
