from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.AvailableEffects - Layer 181
AvailableEffects = typing.Annotated[
    typing.Union[
        types.messages.AvailableEffects,
        types.messages.AvailableEffectsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
