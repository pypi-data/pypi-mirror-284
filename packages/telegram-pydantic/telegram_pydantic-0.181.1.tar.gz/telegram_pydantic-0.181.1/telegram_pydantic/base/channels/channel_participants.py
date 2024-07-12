from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# channels.ChannelParticipants - Layer 181
ChannelParticipants = typing.Annotated[
    typing.Union[
        types.channels.ChannelParticipants,
        types.channels.ChannelParticipantsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
