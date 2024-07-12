from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatParticipant - Layer 181
ChatParticipant = typing.Annotated[
    typing.Union[
        types.ChatParticipant,
        types.ChatParticipantAdmin,
        types.ChatParticipantCreator
    ],
    pydantic.Field(discriminator='QUALNAME')
]
