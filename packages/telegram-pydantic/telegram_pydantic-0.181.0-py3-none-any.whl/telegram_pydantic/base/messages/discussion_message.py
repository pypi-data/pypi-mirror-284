from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.DiscussionMessage - Layer 181
DiscussionMessage = typing.Annotated[
    typing.Union[
        types.messages.DiscussionMessage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
