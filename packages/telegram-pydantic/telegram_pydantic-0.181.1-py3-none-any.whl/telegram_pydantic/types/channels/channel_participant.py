from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipant(BaseModel):
    """
    types.channels.ChannelParticipant
    ID: 0xdfb80317
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.ChannelParticipant'] = pydantic.Field(
        'types.channels.ChannelParticipant',
        alias='_'
    )

    participant: "base.ChannelParticipant"
    chats: list["base.Chat"]
    users: list["base.User"]
