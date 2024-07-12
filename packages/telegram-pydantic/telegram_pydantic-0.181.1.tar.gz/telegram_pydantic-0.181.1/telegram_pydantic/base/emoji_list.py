from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EmojiList - Layer 181
EmojiList = typing.Annotated[
    typing.Union[
        types.EmojiList,
        types.EmojiListNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
