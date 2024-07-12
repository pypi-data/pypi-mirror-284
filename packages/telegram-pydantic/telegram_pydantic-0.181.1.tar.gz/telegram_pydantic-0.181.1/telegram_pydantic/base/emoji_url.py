from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EmojiURL - Layer 181
EmojiURL = typing.Annotated[
    typing.Union[
        types.EmojiURL
    ],
    pydantic.Field(discriminator='QUALNAME')
]
