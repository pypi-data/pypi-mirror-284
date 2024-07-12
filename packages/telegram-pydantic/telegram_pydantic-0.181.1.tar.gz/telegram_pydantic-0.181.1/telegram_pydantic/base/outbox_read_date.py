from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# OutboxReadDate - Layer 181
OutboxReadDate = typing.Annotated[
    typing.Union[
        types.OutboxReadDate
    ],
    pydantic.Field(discriminator='QUALNAME')
]
