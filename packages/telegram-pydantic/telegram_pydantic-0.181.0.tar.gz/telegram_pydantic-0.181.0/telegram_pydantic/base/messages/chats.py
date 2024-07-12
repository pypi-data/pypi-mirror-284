from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.Chats - Layer 181
Chats = typing.Annotated[
    typing.Union[
        types.messages.Chats,
        types.messages.ChatsSlice
    ],
    pydantic.Field(discriminator='QUALNAME')
]
