from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageReplyHeader - Layer 181
MessageReplyHeader = typing.Annotated[
    typing.Union[
        types.MessageReplyHeader,
        types.MessageReplyStoryHeader
    ],
    pydantic.Field(discriminator='QUALNAME')
]
