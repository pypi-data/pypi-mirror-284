from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChannelParticipant - Layer 181
ChannelParticipant = typing.Annotated[
    typing.Union[
        types.ChannelParticipant,
        types.ChannelParticipantAdmin,
        types.ChannelParticipantBanned,
        types.ChannelParticipantCreator,
        types.ChannelParticipantLeft,
        types.ChannelParticipantSelf
    ],
    pydantic.Field(discriminator='QUALNAME')
]
