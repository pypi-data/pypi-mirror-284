from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# contacts.Blocked - Layer 181
Blocked = typing.Annotated[
    typing.Union[
        types.contacts.Blocked,
        types.contacts.BlockedSlice
    ],
    pydantic.Field(discriminator='QUALNAME')
]
