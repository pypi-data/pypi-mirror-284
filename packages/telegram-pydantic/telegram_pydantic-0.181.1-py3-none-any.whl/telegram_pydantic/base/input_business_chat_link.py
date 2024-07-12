from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBusinessChatLink - Layer 181
InputBusinessChatLink = typing.Annotated[
    typing.Union[
        types.InputBusinessChatLink
    ],
    pydantic.Field(discriminator='QUALNAME')
]
