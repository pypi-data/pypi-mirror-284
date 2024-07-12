from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EmojiKeyword - Layer 181
EmojiKeyword = typing.Annotated[
    typing.Union[
        types.EmojiKeyword,
        types.EmojiKeywordDeleted
    ],
    pydantic.Field(discriminator='QUALNAME')
]
