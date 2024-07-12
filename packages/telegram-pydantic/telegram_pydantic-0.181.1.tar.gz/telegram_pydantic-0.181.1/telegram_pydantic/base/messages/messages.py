from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.Messages - Layer 181
Messages = typing.Annotated[
    typing.Union[
        types.messages.ChannelMessages,
        types.messages.Messages,
        types.messages.MessagesNotModified,
        types.messages.MessagesSlice
    ],
    pydantic.Field(discriminator='QUALNAME')
]
