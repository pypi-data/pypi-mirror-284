from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EncryptedMessage - Layer 181
EncryptedMessage = typing.Annotated[
    typing.Union[
        types.EncryptedMessage,
        types.EncryptedMessageService
    ],
    pydantic.Field(discriminator='QUALNAME')
]
