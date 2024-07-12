from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# channels.ChannelParticipant - Layer 181
ChannelParticipant = typing.Annotated[
    typing.Union[
        types.channels.ChannelParticipant
    ],
    pydantic.Field(discriminator='QUALNAME')
]
