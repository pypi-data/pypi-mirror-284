from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.TranscribedAudio - Layer 181
TranscribedAudio = typing.Annotated[
    typing.Union[
        types.messages.TranscribedAudio
    ],
    pydantic.Field(discriminator='QUALNAME')
]
