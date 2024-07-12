from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ForumTopic - Layer 181
ForumTopic = typing.Annotated[
    typing.Union[
        types.ForumTopic,
        types.ForumTopicDeleted
    ],
    pydantic.Field(discriminator='QUALNAME')
]
