from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# GroupCallParticipantVideo - Layer 181
GroupCallParticipantVideo = typing.Annotated[
    typing.Union[
        types.GroupCallParticipantVideo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
