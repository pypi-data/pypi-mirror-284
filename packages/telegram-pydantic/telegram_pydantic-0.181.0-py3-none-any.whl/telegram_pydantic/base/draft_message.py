from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# DraftMessage - Layer 181
DraftMessage = typing.Annotated[
    typing.Union[
        types.DraftMessage,
        types.DraftMessageEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
