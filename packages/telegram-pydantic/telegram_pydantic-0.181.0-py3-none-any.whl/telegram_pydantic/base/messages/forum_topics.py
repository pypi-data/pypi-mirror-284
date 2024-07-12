from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.ForumTopics - Layer 181
ForumTopics = typing.Annotated[
    typing.Union[
        types.messages.ForumTopics
    ],
    pydantic.Field(discriminator='QUALNAME')
]
