from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EmojiLanguage - Layer 181
EmojiLanguage = typing.Annotated[
    typing.Union[
        types.EmojiLanguage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
