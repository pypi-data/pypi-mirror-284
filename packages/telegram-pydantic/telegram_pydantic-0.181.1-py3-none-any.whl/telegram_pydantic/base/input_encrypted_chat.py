from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputEncryptedChat - Layer 181
InputEncryptedChat = typing.Annotated[
    typing.Union[
        types.InputEncryptedChat
    ],
    pydantic.Field(discriminator='QUALNAME')
]
