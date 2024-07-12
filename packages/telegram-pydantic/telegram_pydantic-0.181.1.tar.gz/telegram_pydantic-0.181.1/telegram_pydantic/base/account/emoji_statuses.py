from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.EmojiStatuses - Layer 181
EmojiStatuses = typing.Annotated[
    typing.Union[
        types.account.EmojiStatuses,
        types.account.EmojiStatusesNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
