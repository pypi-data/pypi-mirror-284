from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.AffectedFoundMessages - Layer 181
AffectedFoundMessages = typing.Annotated[
    typing.Union[
        types.messages.AffectedFoundMessages
    ],
    pydantic.Field(discriminator='QUALNAME')
]
