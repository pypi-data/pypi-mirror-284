from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EmojiKeywordsDifference - Layer 181
EmojiKeywordsDifference = typing.Annotated[
    typing.Union[
        types.EmojiKeywordsDifference
    ],
    pydantic.Field(discriminator='QUALNAME')
]
