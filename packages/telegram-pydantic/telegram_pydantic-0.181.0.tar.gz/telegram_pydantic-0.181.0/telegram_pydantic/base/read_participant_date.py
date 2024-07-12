from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ReadParticipantDate - Layer 181
ReadParticipantDate = typing.Annotated[
    typing.Union[
        types.ReadParticipantDate
    ],
    pydantic.Field(discriminator='QUALNAME')
]
