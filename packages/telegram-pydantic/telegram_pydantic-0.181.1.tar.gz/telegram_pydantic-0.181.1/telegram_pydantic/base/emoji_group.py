from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EmojiGroup - Layer 181
EmojiGroup = typing.Annotated[
    typing.Union[
        types.EmojiGroup,
        types.EmojiGroupGreeting,
        types.EmojiGroupPremium
    ],
    pydantic.Field(discriminator='QUALNAME')
]
