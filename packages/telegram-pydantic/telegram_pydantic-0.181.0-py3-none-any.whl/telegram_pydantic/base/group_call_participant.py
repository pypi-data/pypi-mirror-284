from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# GroupCallParticipant - Layer 181
GroupCallParticipant = typing.Annotated[
    typing.Union[
        types.GroupCallParticipant
    ],
    pydantic.Field(discriminator='QUALNAME')
]
