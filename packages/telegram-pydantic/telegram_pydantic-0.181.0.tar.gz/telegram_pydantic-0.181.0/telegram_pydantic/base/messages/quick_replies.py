from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.QuickReplies - Layer 181
QuickReplies = typing.Annotated[
    typing.Union[
        types.messages.QuickReplies,
        types.messages.QuickRepliesNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
