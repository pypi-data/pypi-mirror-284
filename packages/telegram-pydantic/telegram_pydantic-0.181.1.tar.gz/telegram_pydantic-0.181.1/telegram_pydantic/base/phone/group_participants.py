from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# phone.GroupParticipants - Layer 181
GroupParticipants = typing.Annotated[
    typing.Union[
        types.phone.GroupParticipants
    ],
    pydantic.Field(discriminator='QUALNAME')
]
