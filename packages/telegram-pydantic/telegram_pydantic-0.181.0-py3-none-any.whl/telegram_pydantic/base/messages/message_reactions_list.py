from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.MessageReactionsList - Layer 181
MessageReactionsList = typing.Annotated[
    typing.Union[
        types.messages.MessageReactionsList
    ],
    pydantic.Field(discriminator='QUALNAME')
]
