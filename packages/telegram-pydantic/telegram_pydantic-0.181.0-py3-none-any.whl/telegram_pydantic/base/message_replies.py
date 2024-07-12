from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageReplies - Layer 181
MessageReplies = typing.Annotated[
    typing.Union[
        types.MessageReplies
    ],
    pydantic.Field(discriminator='QUALNAME')
]
