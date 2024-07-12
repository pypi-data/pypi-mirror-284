from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.EmojiGroups - Layer 181
EmojiGroups = typing.Annotated[
    typing.Union[
        types.messages.EmojiGroups,
        types.messages.EmojiGroupsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
