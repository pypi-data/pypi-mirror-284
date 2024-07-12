from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatParticipants - Layer 181
ChatParticipants = typing.Annotated[
    typing.Union[
        types.ChatParticipants,
        types.ChatParticipantsForbidden
    ],
    pydantic.Field(discriminator='QUALNAME')
]
