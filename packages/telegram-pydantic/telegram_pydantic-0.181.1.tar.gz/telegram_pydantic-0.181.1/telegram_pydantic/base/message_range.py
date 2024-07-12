from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageRange - Layer 181
MessageRange = typing.Annotated[
    typing.Union[
        types.MessageRange
    ],
    pydantic.Field(discriminator='QUALNAME')
]
