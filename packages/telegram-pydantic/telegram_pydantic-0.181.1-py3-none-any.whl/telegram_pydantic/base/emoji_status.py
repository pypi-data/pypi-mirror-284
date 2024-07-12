from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EmojiStatus - Layer 181
EmojiStatus = typing.Annotated[
    typing.Union[
        types.EmojiStatus,
        types.EmojiStatusEmpty,
        types.EmojiStatusUntil
    ],
    pydantic.Field(discriminator='QUALNAME')
]
