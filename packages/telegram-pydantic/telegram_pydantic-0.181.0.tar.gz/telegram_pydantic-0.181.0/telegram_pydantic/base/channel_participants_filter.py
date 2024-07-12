from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChannelParticipantsFilter - Layer 181
ChannelParticipantsFilter = typing.Annotated[
    typing.Union[
        types.ChannelParticipantsAdmins,
        types.ChannelParticipantsBanned,
        types.ChannelParticipantsBots,
        types.ChannelParticipantsContacts,
        types.ChannelParticipantsKicked,
        types.ChannelParticipantsMentions,
        types.ChannelParticipantsRecent,
        types.ChannelParticipantsSearch
    ],
    pydantic.Field(discriminator='QUALNAME')
]
