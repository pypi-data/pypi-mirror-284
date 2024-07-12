from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.AffectedMessages - Layer 181
AffectedMessages = typing.Annotated[
    typing.Union[
        types.messages.AffectedMessages
    ],
    pydantic.Field(discriminator='QUALNAME')
]
