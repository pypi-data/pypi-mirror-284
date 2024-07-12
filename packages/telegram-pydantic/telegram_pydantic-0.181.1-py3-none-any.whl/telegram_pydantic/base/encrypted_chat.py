from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EncryptedChat - Layer 181
EncryptedChat = typing.Annotated[
    typing.Union[
        types.EncryptedChat,
        types.EncryptedChatDiscarded,
        types.EncryptedChatEmpty,
        types.EncryptedChatRequested,
        types.EncryptedChatWaiting
    ],
    pydantic.Field(discriminator='QUALNAME')
]
