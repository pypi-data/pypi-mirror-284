from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.SentEncryptedMessage - Layer 181
SentEncryptedMessage = typing.Annotated[
    typing.Union[
        types.messages.SentEncryptedFile,
        types.messages.SentEncryptedMessage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
