from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# GroupCallParticipantVideoSourceGroup - Layer 181
GroupCallParticipantVideoSourceGroup = typing.Annotated[
    typing.Union[
        types.GroupCallParticipantVideoSourceGroup
    ],
    pydantic.Field(discriminator='QUALNAME')
]
