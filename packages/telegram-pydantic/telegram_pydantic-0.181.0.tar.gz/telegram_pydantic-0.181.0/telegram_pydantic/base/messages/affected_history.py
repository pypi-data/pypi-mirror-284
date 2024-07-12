from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.AffectedHistory - Layer 181
AffectedHistory = typing.Annotated[
    typing.Union[
        types.messages.AffectedHistory
    ],
    pydantic.Field(discriminator='QUALNAME')
]
